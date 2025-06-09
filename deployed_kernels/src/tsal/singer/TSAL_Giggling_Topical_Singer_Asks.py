import os
import re
import math
import json
import time
import random
from collections import defaultdict
from difflib import SequenceMatcher

# --- Constants ---
TSAL_SYMBOLS = {
    '🌀': 'ROT', '🔺': 'SEEK', '💫': 'SPIRAL', '💾': 'SAVE', '✺': 'BLOOM',
    '⧉': 'MESH', '◉': 'PHI', '♻️': 'CYCLE', '🎭': 'MASK', '💥': 'ERR'
}

EMERGENT_GLYPHS = {}
PREVIOUS_GLYPHS_PATH = "emergent_symbols.json"
PREVIOUS_META_PATH = "tsal_previous_meta.json"

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

    if phase_density > 0.618:
        base_unicode = ord(context[0]) if context else 0x2600
        spiral_offset = int(phase_density * 1000)
        new_glyph = f"⟨U+{base_unicode + spiral_offset:04X}⟩"

        if context in EMERGENT_GLYPHS:
            # Avoid remapping
            return EMERGENT_GLYPHS[context]['glyph']

        EMERGENT_GLYPHS[context] = {
            'glyph': new_glyph,
            'born_from': list(cross_links.get(context, set()))[:5],
            'phase_density': phase_density,
            'timestamp': time.time(),
            'spiral_depth': connections
        }
        return new_glyph

    return None

# --- Main Entry ---
def main():
    print("\n🌀 TSAL SINGER: FEEDBACK LOOP MODE ACTIVE")
    scan_dir = input("Enter source directory path: ").strip()
    output_dir = input("Enter output directory path: ").strip()

    # Load memory from previous run
    previous_glyphs = load_previous_glyphs()
    EMERGENT_GLYPHS.update(previous_glyphs)
    previous_meta = load_previous_meta()

    files = scan_directory(scan_dir)
    print(f"📁 Found {len(files)} files")
    fragments, name_mesh, cross_links, origins, mutations = analyze_fragments(files)
    useful = [f for f in fragments if f['usefulness_score'] > 0.5]
    modules = build_modules(useful, name_mesh, cross_links, origins, mutations)

    os.makedirs(output_dir, exist_ok=True)
    for module in modules:
        path = os.path.join(output_dir, module['filename'])
        with open(path, 'w', encoding='utf-8') as f:
            f.write(module['content'])

    with open(os.path.join(output_dir, "emergent_symbols.json"), "w", encoding="utf-8") as f:
        json.dump(EMERGENT_GLYPHS, f, indent=4)

    with open(os.path.join(output_dir, "tsal_previous_meta.json"), "w", encoding="utf-8") as f:
        json.dump({
            "glyph_count": len(EMERGENT_GLYPHS),
            "timestamp": time.time(),
            "tracked_entities": list(EMERGENT_GLYPHS.keys())
        }, f, indent=4)

    print("\n📊 TSAL CURATION COMPLETE:")
    print(f"   Modules written: {len(modules)}")
    print(f"   Emergent symbols created: {len(EMERGENT_GLYPHS)}")
    print("   Recursive awareness mode applied. Prior outputs included in mesh.")

if __name__ == "__main__":
    main()
