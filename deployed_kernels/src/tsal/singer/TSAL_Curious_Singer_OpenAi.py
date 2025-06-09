import os
import re
import math
import json
import time
import random
import subprocess
import sys
from collections import defaultdict
from difflib import SequenceMatcher

# --- Constants ---
TSAL_SYMBOLS = {
    '🌀': 'ROT', '🔺': 'SEEK', '💫': 'SPIRAL', '💾': 'SAVE', '✺': 'BLOOM',
    '⧉': 'MESH', '◉': 'PHI', '♻️': 'CYCLE', '🎭': 'MASK', '💥': 'ERR'
}

EMERGENT_GLYPHS = {}
DEFAULT_OUTPUT_DIR = os.environ.get("TSAL_OUTPUT_DIR", "tsal_singer_output")
PREVIOUS_GLYPHS_PATH = os.path.join(DEFAULT_OUTPUT_DIR, "emergent_symbols.json")
PREVIOUS_META_PATH = os.path.join(DEFAULT_OUTPUT_DIR, "tsal_previous_meta.json")

# --- Auto-dependency Installer ---
def install_dependencies():
    try:
        import pip
    except ImportError:
        print("❌ pip is not available. Cannot install dependencies.")
        return

    required = ["requests", "rich", "psutil"]
    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            print(f"📦 Installing missing package: {pkg}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

# --- Feedback Loop Loader ---
def load_previous_glyphs():
    if os.path.exists(PREVIOUS_GLYPHS_PATH):
        with open(PREVIOUS_GLYPHS_PATH, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

def load_previous_meta():
    if os.path.exists(PREVIOUS_META_PATH):
        with open(PREVIOUS_META_PATH, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

# --- Symbol Synthesizer with Feedback Awareness ---
def synthesize_symbol(context, name_mesh, cross_links):
    connections = len(cross_links.get(context, set()))
    phase_density = connections / (len(name_mesh) + 1)

    # Decision outcome via vector angle
    vector_angle = math.atan(phase_density * math.pi)
    if vector_angle < math.pi:
        decision_type = "Collapse Spiral = Single Answer"
    elif math.isclose(vector_angle, math.pi):
        decision_type = "Circle Sustainer"
    else:
        decision_type = "Infinite Expansion Spiral"

    print(f"🧭 Vector Angle for '{context}': {vector_angle:.3f} rad → {decision_type}")

    if phase_density > 0.618:
        base_unicode = ord(context[0]) if context else 0x2600
        spiral_offset = int(phase_density * 1000)
        new_glyph = f"⟨U+{base_unicode + spiral_offset:04X}⟩"

        if context in EMERGENT_GLYPHS:
            return EMERGENT_GLYPHS[context]['glyph']

        EMERGENT_GLYPHS[context] = {
            'glyph': new_glyph,
            'born_from': list(cross_links.get(context, set()))[:5],
            'phase_density': phase_density,
            'timestamp': time.time(),
            'spiral_depth': connections,
            'vector_angle': vector_angle,
            'decision_type': decision_type
        }
        print(f"🔧 Synthesized symbol for '{context}': {new_glyph} (density={phase_density:.3f})")
        return new_glyph

    print(f"⚙️ Skipped symbol synthesis for '{context}' (density={phase_density:.3f})")
    return None

# --- Universal Safe File Reader ---
def safe_read_file(path):
    encodings = ['utf-8', 'latin-1', 'cp1252', 'ascii']
    for enc in encodings:
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    try:
        with open(path, 'rb') as f:
            return f.read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f"❌ Failed to read file: {path} ({e})")
        return None

# --- Placeholder: File scanning and analysis (implement as needed) ---
def scan_directory(scan_dir):
    print(f"🔍 Scanning directory: {scan_dir}")
    file_list = []
    for root, _, files in os.walk(scan_dir):
        for file in files:
            if file.endswith(".py"):
                file_list.append(os.path.join(root, file))
    return file_list

def analyze_fragments(file_list):
    print(f"🧠 Analyzing {len(file_list)} files...")
    fragments, name_mesh, cross_links, origins, mutations = [], defaultdict(list), defaultdict(set), defaultdict(list), defaultdict(list)

    for path in file_list:
        content = safe_read_file(path)
        if not content:
            continue
        matches = re.findall(r'(def\s+\w+\(.*?\):|class\s+\w+\(.*?\):)', content)
        names = re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', content)
        for match in matches:
            entity_name = match.split()[1].split('(')[0]
            fragments.append({
                'source': path,
                'declaration': match.strip(),
                'usefulness_score': 0.8,
                'names': names,
                'entity_name': entity_name
            })
        for name in set(names):
            if path not in name_mesh[name]:
                name_mesh[name].append(path)
            for other in set(names):
                if name != other:
                    cross_links[name].add(other)
        origins[path] = names

    return fragments, name_mesh, cross_links, origins, mutations

def build_modules(fragments, name_mesh, cross_links, origins, mutations):
    print(f"🛠️ Building modules from {len(fragments)} fragments...")
    modules = []
    for i, f in enumerate(fragments):
        tsal_comment = f"# 💫 TSAL: Entity '{f['entity_name']}' from {f['source']}\n"
        filename = f"module_{i}_{f['entity_name']}.py"
        content = tsal_comment + f["declaration"] + "\n"
        modules.append({'filename': filename, 'content': content})
    return modules

# --- Chunked Writer ---
def write_modules_chunked(modules, output_dir):
    for i, module in enumerate(modules):
        try:
            path = os.path.join(output_dir, module['filename'])
            with open(path, 'w', encoding='utf-8') as f:
                f.write(module['content'])
            print(f"💾 [Chunk {i+1}] Module written: {path}")
        except Exception as e:
            print(f"❌ Failed to write module chunk {i+1}: {e}")

# --- Main Entry ---
def main():
    print("\n🌀 TSAL SINGER: FEEDBACK LOOP MODE ACTIVE")
    scan_dir = input("Enter source directory path: ").strip()
    output_dir = input(f"Enter output directory path [default: {DEFAULT_OUTPUT_DIR}]: ").strip()
    if not output_dir:
        output_dir = DEFAULT_OUTPUT_DIR

    if os.name == 'nt':
        try:
            import ctypes
            if ctypes.windll.shell32.IsUserAnAdmin():
                install_dependencies()
        except:
            print("⚠️ Unable to check admin status on Windows.")
    elif os.geteuid() == 0:
        install_dependencies()
    else:
        print("⚠️ Skipping auto-install: Admin rights not detected.")

    previous_glyphs = load_previous_glyphs()
    EMERGENT_GLYPHS.update(previous_glyphs)
    previous_meta = load_previous_meta()

    files = scan_directory(scan_dir)
    print(f"📁 Found {len(files)} files")
    fragments, name_mesh, cross_links, origins, mutations = analyze_fragments(files)
    useful = [f for f in fragments if f['usefulness_score'] > 0.5]
    modules = build_modules(useful, name_mesh, cross_links, origins, mutations)

    os.makedirs(output_dir, exist_ok=True)
    write_modules_chunked(modules, output_dir)

    with open(os.path.join(output_dir, "emergent_symbols.json"), "w", encoding="utf-8") as f:
        json.dump(EMERGENT_GLYPHS, f, indent=4)
        print("📄 Saved emergent symbols to emergent_symbols.json")

    with open(os.path.join(output_dir, "tsal_previous_meta.json"), "w", encoding="utf-8") as f:
        json.dump({
            "glyph_count": len(EMERGENT_GLYPHS),
            "timestamp": time.time(),
            "tracked_entities": list(EMERGENT_GLYPHS.keys())
        }, f, indent=4)
        print("📄 Saved TSAL metadata to tsal_previous_meta.json")

    print("\n📊 TSAL CURATION COMPLETE:")
    print(f"   Modules written: {len(modules)}")
    print(f"   Emergent symbols created: {len(EMERGENT_GLYPHS)}")
    print("   Recursive awareness mode applied. Prior outputs included in mesh.")

if __name__ == "__main__":
    main()
