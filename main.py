"""
Xiaomi-OCR-0 Production Pipeline
Local Edge Vision-Language Parsing using 4-Bit Quantized Ollama (richardyoung/xiaomi-ocr-0:Q4_K_M)
- Task 1: Interactive Hotkey Bot (F9 / Ctrl+Shift+O) that inspects selected images in Windows Explorer / Clipboard
- Task 2 & 3: Standard programmatic Ollama queries for 1-page complex documents
"""

import os
import sys
import time
import keyboard
import ollama
from rich.console import Console
from rich.panel import Panel

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

console = Console(highlight=False)
MODEL_TAG = "richardyoung/xiaomi-ocr-0:Q4_K_M"

PROMPTS = {
    "task1_math": (
        "Extract all content from this document into clean markdown. "
        "Format all mathematical equations and derivations using valid LaTeX math blocks ($$ ... $$) with equation numbers preserved."
    ),
    "task2_book": (
        "Transcribe all text from this open book spread in natural reading order. "
        "Include all headings, dialogue, and mathematical formulas formatted in LaTeX."
    ),
    "task3_w2": (
        "Extract all fields and values from this tax/financial form into a comprehensive, itemized markdown table."
    )
}


def query_model(image_path: str, prompt_text: str) -> str:
    """Send multimodal OCR query to local 4-bit quantized Xiaomi-OCR-0 via Ollama."""
    abs_path = os.path.abspath(image_path)
    console.print(f"[bold cyan]>> Querying Xiaomi-OCR-0 ({MODEL_TAG})...[/bold cyan]")
    console.print(f"[dim]Artifact: {abs_path}[/dim]")
    response = ollama.chat(
        model=MODEL_TAG,
        messages=[{
            "role": "user",
            "content": prompt_text,
            "images": [abs_path]
        }]
    )
    return response["message"]["content"]

def run_task2_book_page(image_path: str = "inputs/task2_book_page.jpg"):
    """Task 2: Standard Ollama query for full open book spread."""
    transcription = query_model(image_path, PROMPTS["task2_book"])
    
    template_file = "templates/book_page_template.html"
    with open(template_file, "r", encoding="utf-8") as tf:
        template = tf.read()
    
    html_content = template.replace("{{image_path}}", image_path).replace("{{transcription}}", transcription)
    
    out_file = "outputs/task2_book_page_transcription.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)

def get_target_image_from_windows() -> str:
    """
    Intelligently identifies the target image when hotkey is triggered:
    1. Checks the currently selected file in any open Windows Explorer folder.
    2. Checks the Windows Clipboard for copied files or pasted screenshots.
    3. Falls back to default inputs/task1_dense_equations.jpg if no external selection found.
    """
    valid_exts = (".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tif", ".tiff")
    
    # 1. Check active Windows Explorer selected file via Shell COM
    try:
        import win32com.client
        import win32gui
        shell = win32com.client.Dispatch("Shell.Application")
        fg_hwnd = win32gui.GetForegroundWindow()
        for win in shell.Windows():
            if win.HWND == fg_hwnd:
                selected_items = win.Document.SelectedItems()
                if selected_items.Count > 0:
                    item_path = selected_items.Item(0).Path
                    if item_path.lower().endswith(valid_exts):
                        return item_path
    except Exception:
        pass

    # 2. Check Clipboard for copied file path
    try:
        import win32clipboard
        win32clipboard.OpenClipboard()
        try:
            if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_HDROP):
                files = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
                for f in files:
                    if f.lower().endswith(valid_exts):
                        return f
        finally:
            win32clipboard.CloseClipboard()
    except Exception:
        pass

    # 3. Check Clipboard for captured image screenshot
    try:
        from PIL import ImageGrab
        clip_img = ImageGrab.grabclipboard()
        if clip_img is not None:
            temp_path = "inputs/clipboard_capture.png"
            clip_img.save(temp_path)
            return temp_path
    except Exception:
        pass

    # Default fallback to Task 1 primary input artifact
    return "inputs/task1_dense_equations.jpg"


def run_task3_w2_form(image_path: str = "inputs/task3_tax_w2_form.png"):
    """Task 3: Standard Ollama query for official tax & financial forms."""
    audit_data = query_model(image_path, PROMPTS["task3_w2"])
    
    out_file = "outputs/task3_tax_w2_form_audit.md"
    content = f"""# Autonomous Financial Audit Briefing: Key Information Extraction
**Input Artifact**: Official IRS Form W-2 Wage & Tax Statement  
**Input Path**: `{image_path}`  
**Model Runtime**: Xiaomi-OCR-0 (0.8B Q4_K_M Ollama)  
**Timestamp**: {time.strftime('%Y-%m-%d %H:%M:%S')}  

---

## 🧾 Complete Extracted Form Ledger & Audit Breakdown

{audit_data}

---
*Validated locally with Xiaomi-OCR-0 edge vision model.*
"""
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)

def run_task1_hotkey_bot(custom_path: str = None):
    """Task 1: Hotkey-triggered Math & Thesis Companion (LaTeX formula extraction)."""
    target_path = custom_path if custom_path else get_target_image_from_windows()
    raw_ocr = query_model(target_path, PROMPTS["task1_math"])
    
    base_name = os.path.splitext(os.path.basename(target_path))[0]
    out_file = f"outputs/{base_name}_report.md" if base_name.startswith("task1_") else f"outputs/task1_{base_name}_report.md"
    
    content = f"""# Mathematical Thesis & Formula Extraction Report
**Input Artifact**: Mathematical Research Paper / Equation Sheet  
**Input Path**: `{target_path}`  
**Model Runtime**: Xiaomi-OCR-0 (0.8B Q4_K_M Ollama)  
**Mode**: Hotkey Bot Live Ingestion (F9 / Ctrl+Shift+O)  
**Timestamp**: {time.strftime('%Y-%m-%d %H:%M:%S')}  


---

## 📐 Complete Extracted LaTeX Derivations & Technical Prose

{raw_ocr}

---
*Generated autonomously via Xiaomi-OCR-0 local edge vision engine.*
"""
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)
    console.print(f"[bold green]>> [OK] Processed {target_path} -> {out_file}[/bold green]")

def main():
    os.makedirs("inputs", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)
    
    # Run standard programmatic queries for Task 2 and Task 3
    run_task2_book_page("inputs/task2_book_page.jpg")
    run_task3_w2_form("inputs/task3_tax_w2_form.png")
    
    # Register global hotkeys for Task 1
    keyboard.add_hotkey("f9", lambda: run_task1_hotkey_bot())
    keyboard.add_hotkey("ctrl+shift+o", lambda: run_task1_hotkey_bot())
    
    # Process initial Task 1 baseline document
    run_task1_hotkey_bot("inputs/task1_dense_equations.jpg")
    
    # Clean, concise starting message
    console.print("[bold green]>> Xiaomi-OCR-0 Bot is running. Select any math/equation image in Windows Explorer and press [F9] to extract LaTeX into outputs/. Press Ctrl+C to stop.[/bold green]")
    try:
        keyboard.wait()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

