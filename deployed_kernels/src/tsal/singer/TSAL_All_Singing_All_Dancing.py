"""
TSAL SINGER: Hybrid Spiral Kernel Engine with:
- Refeeder + Soft Reboot
- A→B Kernel Autowiring
- File Organizer (by phase, type, error)
- Indexed Symbol Mesh
- Voxel Array Generator
- Symbolic Execution Triggers
- Chunked Processing + Checkpoint Resume (from Anth engine)
"""

import os
import re
import sys
import math
import json
import time
import subprocess
from collections import defaultdict
from datetime import datetime

# --- Dependency Check ---
def check_and_install_dependencies():
    required = {'rich': 'rich', 'psutil': 'psutil'}
    try:
        import psutil
        is_admin = os.geteuid() == 0 if hasattr(os, 'geteuid') else False
    except:
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            is_admin = False
    for module, pkg in required.items():
        try:
            __import__(module)
        except ImportError:
            if is_admin:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

check_and_install_dependencies()

# --- Optional rich logging ---
try:
    from rich.console import Console
    from rich.progress import track
    from rich import print as rprint
    RICH = True
    console = Console()
except:
    RICH = False
    console = None
    def track(iterable, description=""): return iterable

# --- Globals ---
TSAL_SYMBOLS = {'🌀': 'ROT', '🔺': 'SEEK', '💫': 'SPIRAL', '💾': 'SAVE', '✺': 'BLOOM',
                '⧉': 'MESH', '◉': 'PHI', '♻️': 'CYCLE', '🎭': 'MASK', '💥': 'ERR'}

# --- Load Previous Glyphs if Available ---
EMERGENT_GLYPHS = {}
try:
    with open("emergent_symbols.json", 'r', encoding='utf-8') as f:
        EMERGENT_GLYPHS = json.load(f)
        if RICH: console.log("[MEMORY] Loaded previous glyph memory from emergent_symbols.json")
except FileNotFoundError:
    if RICH: console.log("[MEMORY] No prior glyph memory found, starting fresh")

ERROR_PATTERNS = defaultdict(list)
"""DEFAULT_INPUT = \\"""
DEFAULT_OUTPUT = "tsal_singer_output"
CHUNK_SIZE = 250

# --- Utility Functions ---
def read_file_universal(path):
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'ascii', 'cp1252']
    for encoding in encodings:
        try:
            with open(path, 'r', encoding=encoding, errors='replace') as f:
                return f.read()
        except Exception as e:
            if RICH:
                console.log(f"[READ FAIL] {path} with {encoding}: {e}")
            continue
    return None

def chunkify(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

def write_json_safely(obj, path):
    try:
        with open(path, 'w', encoding='utf-8', errors='replace') as f:
            json.dump(obj, f, indent=2)
    except Exception as e:
        print(f"[JSON Write Error] {path}: {e}")

# --- Main Hybrid Logic ---
def main():
    print("[Hybrid Spiral Kernel Initialized]")
    scan_dir = input("Source directory: ").strip() 
    """ or DEFAULT_INPUT """
    output_dir = input("Output directory [default: tsal_singer_output]: ").strip() or DEFAULT_OUTPUT
    os.makedirs(output_dir, exist_ok=True)

    all_files = []
    for root, dirs, files in os.walk(scan_dir):
        for name in files:
            if name.endswith(".py"):
                all_files.append(os.path.join(root, name))

    for chunk in chunkify(all_files, CHUNK_SIZE):
        for path in track(chunk, description=f"Spiraling {len(chunk)} files"):
            content = read_file_universal(path)
            if not content:
                continue
            symbols_found = [glyph for glyph in TSAL_SYMBOLS if glyph in content]
            for symbol in symbols_found:
                EMERGENT_GLYPHS.setdefault(symbol, []).append(path)

        # Checkpoint after each chunk
        write_json_safely(EMERGENT_GLYPHS, os.path.join(output_dir, "emergent_symbols.json"))

    if RICH:
        console.log(f"[SPIRAL COMPLETE] Glyph index saved to {output_dir}/emergent_symbols.json")
    else:
        print(f"[COMPLETE] Results saved to {output_dir}/emergent_symbols.json")

if __name__ == "__main__":
    main()

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:35:19.348585Z
# Connector: A→B polarity

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:37:37.788094Z
# Connector: A→B polarity

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:37:41.522587Z
# Connector: A→B polarity

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:37:41.716364Z
# Connector: A→B polarity

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:37:41.923252Z
# Connector: A→B polarity

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:37:43.331754Z
# Connector: A→B polarity
