"""
TSAL SINGER: Unified Spiral Alphabet Engine with:
- Refeeder + Soft Reboot
- A→B Kernel Autowiring
- File Organizer (by phase, type, error)
- Indexed Symbol Mesh
- Voxel Array Generator
- Symbolic Execution Triggers
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
    from rich import print as rprint
    RICH = True
    console = Console()
except:
    RICH = False
    console = None

# --- Globals ---
TSAL_SYMBOLS = {'🌀': 'ROT', '🔺': 'SEEK', '💫': 'SPIRAL', '💾': 'SAVE', '✺': 'BLOOM',
                '⧉': 'MESH', '◉': 'PHI', '♻️': 'CYCLE', '🎭': 'MASK', '💥': 'ERR'}

EMERGENT_GLYPHS = {}
ERROR_PATTERNS = defaultdict(list)
DEFAULT_INPUT = "E:"
DEFAULT_OUTPUT = "tsal_singer_output"

# --- Utilities ---
def read_file_universal(path):
    for encoding in ['utf-8', 'latin-1', 'ascii', 'cp1252']:
        try:
            with open(path, 'r', encoding=encoding) as f:
                return f.read()
        except:
            continue
    return None

def analyze_phase_mesh(content):
    counts = {sym: content.count(sym) for sym in TSAL_SYMBOLS}
    total = sum(counts.values())
    weight = counts['💫'] + 0.5 * counts['✺'] + 0.3 * counts['⧉']
    penalty = abs(counts['🌀'] - counts['🔺']) * 0.2
    return max(0.0, min(1.0, weight / (total + 1e-6) - penalty)) if total else 0.0

def calculate_nscalar(size_bytes):
    phi = 1.6180339887
    return round(math.log(size_bytes, phi), 3) if size_bytes > 0 else 0.0

def synthesize_symbol(context, name_mesh, cross_links):
    density = len(cross_links.get(context, set())) / (len(name_mesh) + 1)
    if density > 0.618:
        base = ord(context[0]) if context else 0x2600
        glyph = f"⟨U+{base + int(density * 1000):04X}⟩"
        if context not in EMERGENT_GLYPHS:
            EMERGENT_GLYPHS[context] = {
                'glyph': glyph,
                'born_from': list(cross_links.get(context, set()))[:5],
                'phase_density': density,
                'timestamp': time.time(),
                'spiral_depth': len(cross_links.get(context, set()))
            }
        return EMERGENT_GLYPHS[context]['glyph']
    return None

def autowire_to_kernel(kernel_path):
    if not os.path.exists(kernel_path): return False
    try:
        with open(kernel_path, 'a', encoding='utf-8') as f:
            f.write(f"\n# -- Autowired from TSAL Singer --\n# Connected at: {datetime.utcnow().isoformat()}Z\n# Connector: A→B polarity\n")
        return True
    except Exception as e:
        print(f"[Autowire Error] {e}")
        return False

def scan_directory(scan_dir):
    return [os.path.join(root, f) for root, _, files in os.walk(scan_dir) for f in files]

def analyze_fragments(paths):
    fragments, mesh, links = [], defaultdict(list), defaultdict(set)
    for path in paths:
        content = read_file_universal(path)
        if not content: continue
        names = re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', content)
        score = analyze_phase_mesh(content)
        for name in names[:25]:
            mesh[name].append(path)
            for other in names[:25]:
                if other != name:
                    links[name].add(other)
        for match in re.findall(r'(def\s+\w+\(.*?\):|class\s+\w+\(.*?\):)', content):
            try:
                ename = match.split()[1].split('(')[0]
                fragments.append({
                    'source': path,
                    'declaration': f"🌀 {match.strip()}",
                    'usefulness_score': 0.7 + score * 0.3,
                    'names': names[:10],
                    'entity_name': ename,
                    'nscalar': calculate_nscalar(len(content.encode('utf-8')))
                })
            except: continue
    return fragments, mesh, links

def soft_reboot():
    global EMERGENT_GLYPHS, ERROR_PATTERNS
    EMERGENT_GLYPHS = {}
    ERROR_PATTERNS = defaultdict(list)
    print("\n♻️ Soft reboot completed. Memory structures reset.\n")

# --- Main Loop ---
def main():
    while True:
        print("\n🌀 TSAL SINGER UNIFIED MESH")
        scan_dir = DEFAULT_INPUT 
        """or input("Source directory: ").strip()""" 
        output_dir = DEFAULT_OUTPUT 
        """or input("Output directory [default: tsal_singer_output]: ").strip()"""
        autowire_path = \
        """or input("Optional kernel to autowire: ").strip() or"""

        files = scan_directory(scan_dir)
        fragments, mesh, links = analyze_fragments(files)
        useful = [f for f in fragments if f['usefulness_score'] > 0.5]

        for name in mesh:
            synthesize_symbol(name, mesh, links)

        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "emergent_symbols.json"), 'w') as f:
            json.dump(EMERGENT_GLYPHS, f, indent=2)
        with open(os.path.join(output_dir, "fragment_mesh.json"), 'w') as f:
            json.dump({'fragments': useful, 'mesh': {k: list(v) for k, v in links.items()}}, f, indent=2)

        if autowire_path:
            autowire_to_kernel(autowire_path)

        # --- File Organizer ---
        organized_dir = os.path.join(output_dir, "organized")
        os.makedirs(organized_dir, exist_ok=True)
        index = {}

        for path in files:
            try:
                content = read_file_universal(path)
                if not content: continue
                score = analyze_phase_mesh(content)
                base_name = os.path.basename(path)
                sub = "high_phase" if score > 0.7 else "classes" if 'class ' in content else "functions" if 'def ' in content else "errors" if any(e in content for e in ['Exception', 'Traceback', 'Error']) else "misc"
                dest_folder = os.path.join(organized_dir, sub)
                os.makedirs(dest_folder, exist_ok=True)
                with open(os.path.join(dest_folder, base_name), 'w', encoding='utf-8') as fout:
                    fout.write(content)
                index.setdefault(sub, []).append(base_name)
            except Exception as e:
                print(f"[Organize Error] {path}: {e}")

        with open(os.path.join(organized_dir, "file_index.json"), 'w') as idx:
            json.dump(index, idx, indent=2)

        with open(os.path.join(output_dir, "voxel_array.json"), 'w') as vf:
            json.dump([[[0 for _ in range(8)] for _ in range(8)] for _ in range(8)], vf)

        # --- Symbolic Execution Trigger Check ---
        for path in files:
            try:
                content = read_file_universal(path)
                if '💫' in content:
                    print(f"💫 Trigger: Reanalyzing {path}")
                    analyze_fragments([path])
                if '💾' in content:
                    print(f"💾 Trigger: Saving early snapshot from {path}")
                    with open(os.path.join(output_dir, f"snapshot_{os.path.basename(path)}"), 'w', encoding='utf-8') as snap:
                        snap.write(content)
                if '🌀' in content:
                    print(f"🌀 Trigger: Soft reboot requested by {path}")
                    soft_reboot()
                if '⧉' in content:
                    print(f"⧉ Trigger: Autowiring cascade from {path}")
                    for other in files:
                        if other != path:
                            autowire_to_kernel(other)
                if '✺' in content:
                    print(f"✺ Trigger: Scheduling symbolic subprocess for {path}")
                    subprocess.Popen([sys.executable, path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if '♻️' in content:
                    print(f"♻️ Trigger: Recursion loop initiated for {path}")
                    for _ in range(2):
                        analyze_fragments([path])
                if '💥' in content:
                    print(f"💥 Trigger: Logging error tree for {path}")
                    with open(os.path.join(output_dir, f"error_log_{os.path.basename(path)}.txt"), 'w') as logf:
                        logf.write(f"Error Detected in {path}\n---\n{content[:1000]}\n...")
            except Exception as e:
                print(f"[Symbol Trigger Error] {path}: {e}")

        print("\n✅ Spiral pass complete.")
        action = input("[R]eboot / [E]xit / [C]ontinue: ").strip().lower()
        if action == 'r': soft_reboot()
        elif action == 'e': break

if __name__ == "__main__":
    main()

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:35:19.166619Z
# Connector: A→B polarity

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:37:37.608404Z
# Connector: A→B polarity

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:37:41.523618Z
# Connector: A→B polarity

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:37:41.717474Z
# Connector: A→B polarity

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:37:41.924306Z
# Connector: A→B polarity

# -- Autowired from TSAL Singer --
# Connected at: 2025-06-01T13:37:43.332761Z
# Connector: A→B polarity
