import os
import json

# CONFIGURATION
input_path = r"C:\Users\Samuel Howells\Google Drive\Aletheia - Copy\_3d_mesh_nodes.json"
output_dir = r".\mesh_chunks"
chunk_size = 80

print("🚀 Starting JSON slicer")
print(f"📂 Input file: {input_path}")
print(f"📁 Output directory: {output_dir}")
print(f"🔢 Chunk size: {chunk_size}")

# Create output directory
os.makedirs(output_dir, exist_ok=True)
print("✅ Output directory ensured")

# Load the file
print("📥 Loading JSON file...")
with open(input_path, 'r', encoding='utf-8') as f:
    raw = json.load(f)
print("✅ JSON loaded")

# Determine structure and extract node list
if isinstance(raw, dict):
    data = list(raw.values())  # Flatten values from dict of nodes
    print(f"🔍 Top-level structure: dict with {len(data)} node objects")
elif isinstance(raw, list):
    data = raw
    print(f"🔍 Top-level structure: list with {len(data)} entries")
else:
    raise ValueError("❌ Error: JSON root must be list or dict with mesh nodes")

# Slice data
total = len(data)
print(f"🧮 Total nodes: {total}")
chunks = (total + chunk_size - 1) // chunk_size
print(f"📦 Will create {chunks} chunk files")

for i in range(chunks):
    start = i * chunk_size
    end = min(start + chunk_size, total)
    print(f"🔨 Writing chunk {i+1}/{chunks} | Nodes {start}–{end-1}")

    chunk_data = data[start:end]
    output_file = os.path.join(output_dir, f"mesh_chunk_{i+1:03}.json")

    with open(output_file, 'w', encoding='utf-8') as out_f:
        json.dump(chunk_data, out_f, indent=2)

    print(f"✅ Chunk {i+1} written to {output_file}")

print("🎉 Slicing complete.")
