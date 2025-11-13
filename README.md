<!-- PROJECT BANNER -->
<p align="center">
  <img src="https://img.shields.io/badge/AI%20Pull%20Request%20Reviewer-Offline%20LLM-blue?style=for-the-badge&logo=github" />
</p>

<h1 align="center">🤖 AI Pull Request Reviewer (Offline Local LLM)</h1>

<p align="center">
A fully offline, privacy-safe <b>AI-powered Pull Request Reviewer</b> built using the Qwen LLM.<br>
No API keys • No cloud • Runs fully offline after first run.
</p>

---

## 🔥 Badges

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/LLM-Qwen%200.5B-green" />
  <img src="https://img.shields.io/badge/AI-Offline-red?logo=brain" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey" />
</p>

---

## 🖼 Example Output

![Demo Output](https://github.com/keshavaraj-bit/ai-pr-reviewer/blob/main/Screenshot%202025-11-13%20131128.png?raw=true)

---

## Features

- **Offline Local AI (Qwen 0.5B)** – runs completely on CPU  
- **100% Private** – your code NEVER leaves your machine  
- **Auto-downloads model** into `models/`  
- **Analyzes git diffs** and generates structured reviews  
- **Strict JSON output:**  

```json
```json
{
  "summary": "",
  "issues": [],
  "suggestions": [],
  "tests_needed": [],
  "confidence": 0.0
}
