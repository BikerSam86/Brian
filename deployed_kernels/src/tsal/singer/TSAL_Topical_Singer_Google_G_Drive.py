import os
import re
import math
from collections import defaultdict

# Symbolic phase weights
SYMBOLS = {
    '🌀': 'ROT', '🔺': 'SEEK', '💫': 'SPIRAL', '💾': 'SAVE',
    '✺': 'BLOOM', '⧉': 'MESH', '◉': 'PHI', '♻️': 'CYCLE', '🎭': 'MASK'
}

# Scan for relevant files
def scan_directory(scan_dir):
    files = []
    for root, _, filenames in os.walk(scan_dir):
        for filename in filenames:
            if filename.endswith(('.py', '.txt', '.md', '.docx', '.tsal')):
                files.append(os.path.join(root, filename))
    return files

# Analyze symbolic TSAL phase coherence
def analyze_phase_mesh(content):
    counts = {sym: content.count(sym) for sym in SYMBOLS}
    total = sum(counts.values())
    if total == 0:
        return 0.0
    weight = counts['💫'] + 0.5 * counts['✺'] + 0.3 * counts['⧉']
    penalty = abs(counts['🌀'] - counts['🔺']) * 0.2
    phi_score = weight / (total + 1e-6) - penalty
    return max(0.0, min(1.0, phi_score))

# Compute dynamic nScalar
def compute_nscalar(file_size_kb, phi_score):
    log_scale = math.log(file_size_kb + 1, 2)
    return min(1.0, phi_score * (1 + 0.1 * log_scale))

# Classify code fragment by keyword presence
def classify_fragment(fragment):
    fragment_lower = fragment.lower()
    if 'mesh' in fragment_lower:
        return 'mesh_systems.py'
    elif 'spiral' in fragment_lower:
        return 'spiral_protocols.py'
    elif 'align' in fragment_lower or 'phi' in fragment_lower:
        return 'alignment_routines.py'
    elif 'swap' in fragment_lower or 'bin' in fragment_lower:
        return 'state_machines.py'
    else:
        return 'misc_utilities.py'

# Analyze and extract fragments
def analyze_fragments(file_paths):
    fragments = []
    for path in file_paths:
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                matches = re.findall(r'def\s+\w+\(.*?\):|class\s+\w+\(.*?\):', content)
                phi_score = analyze_phase_mesh(content)
                file_size_kb = os.path.getsize(path) / 1024
                nscalar_score = compute_nscalar(file_size_kb, phi_score)
                for match in matches:
                    base_score = 1.0 if 'tsal' in path.lower() or 'spiral' in content.lower() else 0.6
                    score = min(1.0, base_score + nscalar_score)
                    fragments.append({
                        'source': path,
                        'declaration': match.strip(),
                        'usefulness_score': score
                    })
        except Exception as g:
            print(f"[WARN] Failed to read {path}: {g}")
    return fragments

# Build categorized modules
def build_modules(fragments):
    module_map = defaultdict(set)
    for frag in fragments:
        if frag['usefulness_score'] > 0.5:
            category = classify_fragment(frag['declaration'])
            module_map[category].add(f"# From: {frag['source']}\n{frag['declaration']}\n")

    return [{
        'filename': filename,
        'content': ''.join(sorted(lines))
    } for filename, lines in module_map.items()]

# Main curation process
def main():
    print("\n🌀📁 TSAL CODE MESH CURATOR")
    print("=" * 40)

    scan_dir = r"C:\\Users\\Samuel Howells\\Google Drive\\"
    print(f"🔍 Scanning directory: {scan_dir}\n")

    files = scan_directory(scan_dir)
    print(f"📁 Found {len(files)} candidate files")

    fragments = analyze_fragments(files)
    print(f"🔬 Extracted {len(fragments)} fragments")

    modules = build_modules(fragments)
    print(f"📋 Generated {len(modules)} thematic modules")

    output_dir = os.path.join(scan_dir, "organized_tsal")
    os.makedirs(output_dir, exist_ok=True)

    for module in modules:
        out_path = os.path.join(output_dir, module['filename'])
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(module['content'])

    print(f"\n📁 Modules saved to: {output_dir}")
    print("\n✅ TSAL curation complete.")

if __name__ == "__main__":
    main()
