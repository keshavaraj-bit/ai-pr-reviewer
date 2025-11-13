import sys
import re
import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Color codes
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
MODEL_PATH = r"D:\ai-pr-reviewer\models\Qwen-0.5B"

print("Loading model (downloads only once)...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, cache_dir=MODEL_PATH, dtype=torch.float32)

def load_diff(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def build_prompt(diff):
    return f"""
You are an expert code reviewer.

Return ONLY valid JSON following this exact structure:

{{
  "summary": "",
  "issues": [],
  "suggestions": [],
  "tests_needed": [],
  "confidence": 0.0
}}

Diff:
{diff}

Return ONLY the JSON:
"""

def run_local_model(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=400,
        do_sample=True,
        temperature=0.5
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def sanitize_json(text):
    match = re.search(r"\{.*?\}", text, re.DOTALL)
    if not match:
        return None

    json_str = match.group(0)
    json_str = re.sub(r",\s*}", "}", json_str)
    json_str = re.sub(r",\s*]", "]", json_str)

    try:
        return json.loads(json_str)
    except:
        return None

def print_pretty(data):
    print(f"{GREEN}Summary:{RESET} {data['summary']}\n")

    print(f"{RED}Issues:{RESET}")
    if len(data["issues"]) == 0:
        print("  - None\n")
    else:
        for issue in data["issues"]:
            print("  -", issue)
        print()

    print(f"{BLUE}Suggestions:{RESET}")
    if len(data["suggestions"]) == 0:
        print("  - None\n")
    else:
        for s in data["suggestions"]:
            print("  -", s)
        print()

    print(f"{YELLOW}Tests Needed:{RESET}")
    if len(data["tests_needed"]) == 0:
        print("  - None\n")
    else:
        for t in data["tests_needed"]:
            print("  -", t)
        print()

    print(f"{GREEN}Confidence:{RESET} {data['confidence']}\n")

def save_to_file(data):
    with open("review.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Saved output → review.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python review.py <diff_file>")
        exit(1)

    diff = load_diff(sys.argv[1])
    prompt = build_prompt(diff)

    print("\nReviewing Pull Request locally...\n")

    raw = run_local_model(prompt)
    data = sanitize_json(raw)

    print("Review completed:\n")

    if data:
        print_pretty(data)
        save_to_file(data)
    else:
        print("⚠ Could not extract clean JSON.\n")
        print(raw)
