<div align="center">
  <a href="https://youtu.be/2AGXYEQDa-E">
    <img src="https://img.youtube.com/vi/2AGXYEQDa-E/0.jpg" alt="Xiaomi OCR 0: The 0.8B AI That Destroys Qwen 3.5 on CPU!">
  </a>
  <h3>📺 <a href="https://youtu.be/2AGXYEQDa-E">Watch the full tutorial on YouTube</a></h3>
</div>


# Xiaomi-OCR-0: Unified 0.8B Edge Document Engine

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Model Size](https://img.shields.io/badge/Parameters-0.8B%20Unified-orange.svg)](https://huggingface.co/SeerRay-Lab/Xiaomi-OCR-0)
[![Real5 Benchmark](https://img.shields.io/badge/Real5--OmniDocBench-%231%20Rank%20(95.24)-emerald.svg)](https://arxiv.org/abs/2609.36136)
[![Local Footprint](https://img.shields.io/badge/VRAM%20Footprint-~700%20MB%20(Q4__K__M)-purple.svg)](https://ollama.com/richardyoung/xiaomi-ocr-0)

> "Xiaomi-OCR-0 is an ultra-compact 0.8B vision-language model purpose-built by Xiaomi Research for document parsing, formula extraction, and OCR-centric visual understanding. Outperforming 2B and 4B models on real-world recaptured scans, it runs completely offline on consumer hardware."


---

## 📊 Production Test Workflows

| Workflow | Capability Tested | Input Artifact | Expected Deliverable | Mode |
| :--- | :--- | :--- | :--- | :--- |
| **Task 1: Math & Thesis Companion** | Complex mathematical formula parsing & layout conversion | Academic chunkwise matrix derivation scan | Structured mathematical report with complete compiled LaTeX equations & technical prose | **Hotkey Bot (F9 / Ctrl+Shift+O)** |
| **Task 2: Printed Book Digitizer** | High-density multi-paragraph typography & reading order extraction | Classical literature printed book spread scan | Interactive dual-pane side-by-side reading view with clean text flow | Standard Ollama Query |
| **Task 3: Offline Tax & Financial Auditor** | Key Information Extraction (KIE) & structured grid auditing | US IRS Wage & Tax Statement form photo | Formatted financial audit briefing with complete itemized box verification table | Standard Ollama Query |

---

## ⚡ Quick Start

```powershell
# Step 1: Create virtual environment & install dependencies
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install ollama keyboard pillow rich pywin32

# Step 2: Pull the 4-bit quantized vision model in Ollama
ollama pull richardyoung/xiaomi-ocr-0:Q4_K_M
```


```powershell
# Step 2: Run Production Pipeline
# - Executes standard Ollama queries for Tasks 2 & 3
# - Starts background Hotkey Bot (F9 / Ctrl+Shift+O) for Task 1 on any selected image in Windows Explorer
python main.py
```


---

## 🎯 Practical Use Cases

- 🛡️ **Air-Gapped Document Processing**: Transcribe highly sensitive medical records, contracts, and financial statements with zero cloud leakage on edge laptops.
- 📐 **Academic Research & LaTeX Digitization**: Instantaneous extraction of dense multi-line mathematical equations and OTSL matrix structures directly from scanned textbook pages.
- ✍️ **Archival Heritage Preservation**: Digitize historical cursive scrolls, seal scripts, and degraded library manuscripts that break generic commercial OCR engines.
- 🧾 **Autonomous Expense & Audit Ingestion**: Edge KIE parsing for noisy smartphone receipts, tax invoices, and shipping bills directly into financial workflows.

---

## 🗺️ Future Feature Roadmap

- ⚡ **Native C++ Llama.cpp Subprocess Bindings**: Direct standalone binary execution with zero background daemon overhead.
- 🌐 **Multi-Lingual CPT Expansion**: Broader script coverage beyond English and Simplified Chinese for global heritage archives.
- 🔍 **Interactive WebUI & Bounding Box Visualizer**: Side-by-side polygon alignment viewer for deep document layout quality assurance.
- 📱 **Mobile Edge NInfer Runtime**: Real-time camera stream parsing compiled directly for on-device mobile hardware.

---

<sub>**Keywords:** Xiaomi OCR, Xiaomi 0.8B, local OCR, offline OCR, document AI, CPU OCR, document parsing, offline parsing, secure OCR, text recognition, vision model, local vision, offline extraction, receipt AI, invoice AI, Xiaomi OCR 0, Xiaomi OCR model, Xiaomi OCR Ollama, Xiaomi OCR 0.8B, Xiaomi AI OCR, Xiaomi OCR local, open source OCR, OCR model, math OCR, handwriting OCR, cursive OCR, invoice extraction AI, receipt OCR, OCR benchmark, Xiaomi vs Qwen, local document AI</sub>


