import os
import re
import math
from collections import defaultdict

# --- Constants ---
TSAL_SYMBOLS = {
    '🌀': 'ROT', '🔺': 'SEEK', '💫': 'SPIRAL', '💾': 'SAVE', '✺': 'BLOOM',
    '⧉': 'MESH', '◉': 'PHI', '♻️': 'CYCLE', '🎭': 'MASK', '💥': 'ERR'
}

# --- Helper: Scan directories ---
def scan_directory(scan_dir):
    files = []
    for root, _, filenames in os.walk(scan_dir):
        for filename in filenames:
            if filename.endswith(('.py', '.txt', '.md', '.tsal')):
                files.append(os.path.join(root, filename))
    return files

# --- Helper: Analyze symbolic content ---
def analyze_phase_mesh(content):
    counts = {sym: content.count(sym) for sym in TSAL_SYMBOLS}
    total = sum(counts.values())
    if total == 0:
        return 0.0
    weight = counts['💫'] + 0.5 * counts['✺'] + 0.3 * counts['⧉']
    penalty = abs(counts['🌀'] - counts['🔺']) * 0.2
    phi_score = weight / (total + 1e-6) - penalty
    return max(0.0, min(1.0, phi_score))

# --- Helper: Compute nScalar ---
def compute_nscalar(file_size_kb, phi_score):
    log_scale = math.log(file_size_kb + 1, 2)
    return min(1.0, phi_score * (1 + 0.1 * log_scale))

# --- Helper: Extract and score fragments ---
def analyze_fragments(file_paths):
    fragments = []
    name_mesh = defaultdict(list)

    for path in file_paths:
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                matches = re.findall(r'def\s+\w+\(.*?\):|class\s+\w+\(.*?\):', content)
                names = re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', content)

                phi_score = analyze_phase_mesh(content)
                file_size_kb = os.path.getsize(path) / 1024
                nscalar_score = compute_nscalar(file_size_kb, phi_score)

                for match in matches:
                    base_score = 1.0 if 'tsal' in path.lower() or 'spiral' in content.lower() else 0.6
                    score = min(1.0, base_score + nscalar_score)
                    fragments.append({
                        'source': path,
                        'declaration': match.strip(),
                        'usefulness_score': score,
                        'names': names
                    })

                for name in set(names):
                    name_mesh[name].append(path)

        except Exception as e:
            print(f"[WARN] Failed to read {path}: {e}")

    return fragments, name_mesh

# --- Helper: Build modules with naming ---
def build_modules(fragments, name_mesh):
    module_map = {}
    for frag in fragments:
        themename = "_".join(sorted(set(frag['names']))) if frag['names'] else "anon"
        modname = f"{themename}_vectorized.py"
        if modname not in module_map:
            module_map[modname] = []
        module_map[modname].append(f"# From: {frag['source']}\n{frag['declaration']}\n")

    modules = []
    for modname, lines in module_map.items():
        modules.append({
            'filename': modname,
            'content': '\n'.join(lines)
        })
    return modules

# --- Main Entry ---
def main():
    print("\n🌀 TSAL SINGER: SYMBOLIC NAMING + ERROR DIGNITY")
    scan_dir = input("Enter source directory path: ").strip()
    output_dir = input("Enter output directory path: ").strip()

    files = scan_directory(scan_dir)
    print(f"📁 Found {len(files)} files")

    fragments, name_mesh = analyze_fragments(files)
    useful = [f for f in fragments if f['usefulness_score'] > 0.5]

    modules = build_modules(useful, name_mesh)
    os.makedirs(output_dir, exist_ok=True)
    for module in modules:
        path = os.path.join(output_dir, module['filename'])
        with open(path, 'w', encoding='utf-8') as f:
            f.write(module['content'])

    print("\n📊 TSAL CURATION COMPLETE:")
    print(f"   Modules written: {len(modules)}")
    print(f"   Name vectors detected: {len(name_mesh)}")
    print("   Mesh enriched with temporal naming & error dignity")

if __name__ == "__main__":
    main()
