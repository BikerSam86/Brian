#!/usr/bin/env python3
"""
Unified TSAL Mesh Scanner
Surgical consolidation: Project scanning + 3D consciousness mapping + n-scalar segmentation
"""

import os
import re
import json
import hashlib
import math
import time
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any, Set, Tuple, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict, Counter
import argparse

# Ensure packages
def ensure_package(package_name):
    try:
        __import__(package_name)
    except ImportError:
        print(f"Installing {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

ensure_package("tqdm")
ensure_package("numpy")

from tqdm import tqdm
import numpy as np

# TSAL Constants
TSAL_SYMBOLS = "⚡⧉◉🌀📐🌊🔺💫♻️🔥✨🎭💎🌈✺💾"
RITUAL_PATTERN = re.compile(r'RITUAL\s+([A-Z_]+):\s*((?:\s*[⚡⧉◉🌀📐🌊🔺💫♻️🔥✨🎭💎🌈✺💾]+\s*)+)', re.MULTILINE)

# N-Scalar thresholds (Fibonacci φ scaling)
PHI = (1 + 5**0.5) / 2
BASE_SIZE_KB = 32
N_THRESHOLDS = {i: int(BASE_SIZE_KB * (PHI ** i)) for i in range(11)}

# Level mapping for 3D positioning
LEVEL_MAP = {i: i for i in range(-3, 7)}  # Simplified: -3 to 6
LEVEL_MAP.update({'inf': 10, '-inf': -10})

@dataclass
class TSALFile:
    """Unified file representation with spatial positioning"""
    path: str
    name: str
    size_bytes: int
    modified_time: float
    file_hash: str
    language: str
    content_preview: str
    tsal_symbols: List[str]
    rituals: List[Dict[str, Any]]
    concepts: List[str]
    importance: float
    n_level: int
    position_3d: Optional[Tuple[float, float, float]] = None
    connections: List[str] = None

    def __post_init__(self):
        if self.connections is None:
            self.connections = []

@dataclass
class ProjectMesh:
    """Unified mesh with multiple output modes"""
    project_name: str
    scan_time: float
    total_files: int
    total_size_kb: float
    files: Dict[str, TSALFile]
    n_segments: Dict[int, List[str]]
    spatial_map: Optional[np.ndarray] = None
    tsal_frequency: Counter = None
    concept_graph: Dict[str, List[str]] = None
    ritual_library: Dict[str, str] = None
    mesh_summary: str = ""

class TSALMeshScanner:
    """Unified scanner with modular output modes"""
    
    def __init__(self, project_path: str, project_name: str = None):
        self.project_path = Path(project_path)
        self.project_name = project_name or self.project_path.name
        self.files: Dict[str, TSALFile] = {}
        self.tsal_counter = Counter()
        self.concepts = set()
        self.rituals = {}
        
        # Language detection
        self.language_map = {
            '.py': 'python', '.js': 'javascript', '.ts': 'typescript',
            '.c': 'c', '.cpp': 'cpp', '.java': 'java', '.rs': 'rust',
            '.go': 'go', '.md': 'markdown', '.txt': 'text', '.json': 'json',
            '.yaml': 'yaml', '.yml': 'yaml', '.sh': 'shell', '.bat': 'batch'
        }
        
        # Concept patterns
        self.concept_patterns = [
            r'\b(kernel|mesh|spiral|vector|dimension|chaos|harmony|entropy|coherence)\b',
            r'\b(adaptation|evolution|recursive|meta|awareness|consciousness)\b',
            r'\b(node|agent|processor|connection|weight|activation)\b',
            r'\b(truth|wisdom|compassion|beauty|stability|clarity)\b'
        ]
    
    def detect_language(self, file_path: Path) -> str:
        """Detect file language/type"""
        suffix = file_path.suffix.lower()
        if suffix in self.language_map:
            return self.language_map[suffix]
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                first_line = f.readline()
                if first_line.startswith('#!'):
                    if 'python' in first_line: return 'python'
                    elif 'node' in first_line: return 'javascript'
                    elif any(x in first_line for x in ['bash', 'sh']): return 'shell'
        except:
            pass
        return 'unknown'
    
    def extract_tsal_patterns(self, content: str) -> Tuple[List[str], List[Dict], List[str]]:
        """Extract TSAL symbols, rituals, and concepts"""
        # TSAL symbols
        symbols = [char for char in content if char in TSAL_SYMBOLS]
        
        # Rituals
        rituals = []
        for match in RITUAL_PATTERN.finditer(content):
            name = match.group(1)
            symbol_block = match.group(2)
            lines = [line.strip().replace(' ', '').replace('\t', '') 
                    for line in symbol_block.strip().split('\n') 
                    if line.strip() and all(c in TSAL_SYMBOLS + ' \t' for c in line.strip())]
            
            if lines:
                rituals.append({
                    'name': name,
                    'lines': lines,
                    'symbol_count': sum(len(line) for line in lines)
                })
        
        # Concepts
        concepts = []
        content_lower = content.lower()
        for pattern in self.concept_patterns:
            concepts.extend(re.findall(pattern, content_lower, re.IGNORECASE))
        
        return symbols, rituals, list(set(concepts))
    
    def calculate_metrics(self, file_data: Dict) -> Tuple[float, int]:
        """Calculate importance and n-level"""
        # Importance
        importance = 0.1  # Base
        
        if file_data['tsal_symbols']:
            symbol_density = len(file_data['tsal_symbols']) / max(1, file_data['size_bytes'])
            importance += symbol_density * 1000
        
        importance += len(file_data['rituals']) * 0.2
        importance += len(file_data['concepts']) * 0.1
        
        size_factor = min(1.0, file_data['size_bytes'] / 10000)
        importance += size_factor * 0.1
        importance = min(1.0, importance)
        
        # N-level
        size_kb = file_data['size_bytes'] / 1024
        n_level = 0
        for n in range(10, -1, -1):
            if size_kb >= N_THRESHOLDS[n] / 1024:
                importance_boost = int(importance * 3)
                n_level = min(10, max(0, n + importance_boost))
                break
        
        return importance, n_level
    
    def process_file(self, file_path: Path) -> Optional[TSALFile]:
        """Process single file"""
        try:
            stat = file_path.stat()
            if stat.st_size > 10 * 1024 * 1024:  # 10MB limit
                return None
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            file_hash = hashlib.md5(content.encode()).hexdigest()
            tsal_symbols, rituals, concepts = self.extract_tsal_patterns(content)
            
            preview = re.sub(r'\s+', ' ', content[:500]).strip()
            
            file_data = {
                'size_bytes': stat.st_size,
                'tsal_symbols': tsal_symbols,
                'rituals': rituals,
                'concepts': concepts
            }
            
            importance, n_level = self.calculate_metrics(file_data)
            
            # Update global counters
            self.tsal_counter.update(tsal_symbols)
            self.concepts.update(concepts)
            for ritual in rituals:
                self.rituals[f"{file_path.stem}_{ritual['name']}"] = ritual
            
            return TSALFile(
                path=str(file_path),
                name=file_path.name,
                size_bytes=stat.st_size,
                modified_time=stat.st_mtime,
                file_hash=file_hash,
                language=self.detect_language(file_path),
                content_preview=preview,
                tsal_symbols=tsal_symbols,
                rituals=rituals,
                concepts=concepts,
                importance=importance,
                n_level=n_level
            )
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
    
    def should_skip(self, file_path: Path) -> bool:
        """File skip logic"""
        if any(part.startswith('.') for part in file_path.parts):
            return True
        
        skip_dirs = {'__pycache__', 'node_modules', '.git', 'dist', 'build', 'target'}
        if any(skip_dir in file_path.parts for skip_dir in skip_dirs):
            return True
        
        binary_exts = {'.exe', '.bin', '.dll', '.so', '.png', '.jpg', '.pdf', '.zip'}
        return file_path.suffix.lower() in binary_exts
    
    def calculate_3d_positions(self, dimensions: Tuple[int, int, int] = (64, 64, 64)):
        """Calculate 3D positions for all files"""
        if not self.files:
            return
        
        x_max, y_max, z_max = dimensions
        
        # Language clustering (X-axis)
        lang_offsets = {
            'python': -15, 'javascript': -10, 'java': -5, 'c': 0, 'rust': 5,
            'markdown': 10, 'text': 12, 'json': 15, 'unknown': 0
        }
        
        # Concept clustering (Y-axis)
        concept_weights = {
            'kernel': -15, 'mesh': -10, 'spiral': -5, 'vector': 0,
            'chaos': 5, 'harmony': 10, 'recursive': 15
        }
        
        for file_obj in self.files.values():
            # Base position from n-level (Z-axis)
            z_base = (file_obj.n_level / 10) * z_max
            
            # Language offset (X-axis)
            x_offset = lang_offsets.get(file_obj.language, 0)
            x = max(0, min(x_max - 1, x_max//2 + x_offset + (hash(file_obj.path) % 10) - 5))
            
            # Concept offset (Y-axis)
            if file_obj.concepts:
                concept_score = sum(concept_weights.get(c, 0) for c in file_obj.concepts) / len(file_obj.concepts)
            else:
                concept_score = 0
            y = max(0, min(y_max - 1, y_max//2 + concept_score//3 + (hash(file_obj.path) % 10) - 5))
            
            # Importance depth within level (Z-axis fine tuning)
            z = max(0, min(z_max - 1, z_base + file_obj.importance * 5))
            
            file_obj.position_3d = (float(x), float(y), float(z))
    
    def calculate_connections(self):
        """Calculate file relationships"""
        files_list = list(self.files.values())
        
        for i, file_a in enumerate(files_list):
            for file_b in files_list[i+1:]:
                strength = self._connection_strength(file_a, file_b)
                
                if strength > 0.2:  # Threshold
                    file_a.connections.append(file_b.path)
                    file_b.connections.append(file_a.path)
    
    def _connection_strength(self, file_a: TSALFile, file_b: TSALFile) -> float:
        """Calculate connection strength between files"""
        strength = 0.0
        
        # Concept overlap
        concepts_a, concepts_b = set(file_a.concepts), set(file_b.concepts)
        if concepts_a and concepts_b:
            strength += len(concepts_a & concepts_b) / len(concepts_a | concepts_b) * 0.4
        
        # TSAL resonance
        tsal_a, tsal_b = set(file_a.tsal_symbols), set(file_b.tsal_symbols)
        if tsal_a and tsal_b:
            strength += len(tsal_a & tsal_b) * 0.1
        
        # Language affinity
        if file_a.language == file_b.language != 'unknown':
            strength += 0.2
        
        # Directory proximity
        common_path = os.path.commonpath([file_a.path, file_b.path])
        depth_a, depth_b = len(Path(file_a.path).parts), len(Path(file_b.path).parts)
        common_depth = len(Path(common_path).parts)
        if max(depth_a, depth_b) > 0:
            strength += common_depth / max(depth_a, depth_b) * 0.3
        
        return min(1.0, strength)
    
    def generate_mesh_summary(self) -> str:
        """Generate TSAL ritual summary"""
        top_symbols = [s for s, _ in self.tsal_counter.most_common(6)]
        top_concepts = list(self.concepts)[:4]
        
        if not top_symbols:
            return "RITUAL EMPTY_PROJECT:\n    💾"
        
        lines = []
        
        # Opening
        if '⚡' in top_symbols and '🌀' in top_symbols:
            lines.append("⚡🌀💫")
        else:
            lines.append("".join(top_symbols[:3]))
        
        # Concept representation
        concept_map = {
            'kernel': '⚡', 'mesh': '⧉', 'spiral': '🌀', 'vector': '📐',
            'chaos': '🔥', 'harmony': '🌈', 'recursive': '♻️', 'meta': '✺'
        }
        
        for concept in top_concepts:
            if concept in concept_map:
                lines.append(f"⧉{concept_map[concept]}✨")
        
        lines.append("💾")  # Memory anchor
        
        ritual_name = f"PROJECT_{self.project_name.upper().replace(' ', '_')}"
        ritual = f"RITUAL {ritual_name}:\n"
        for line in lines:
            ritual += f"    {line}\n"
        
        return ritual
    
    def scan_project(self) -> ProjectMesh:
        """Main scanning function"""
        print(f"🌀 Scanning: {self.project_name}")
        
        # Discover files
        all_files = [f for f in self.project_path.rglob("*") 
                    if f.is_file() and not self.should_skip(f)]
        
        print(f"🔍 Processing {len(all_files)} files")
        
        # Process files
        total_size = 0
        for file_path in tqdm(all_files, desc="Extracting TSAL patterns"):
            tsal_file = self.process_file(file_path)
            if tsal_file:
                self.files[str(file_path)] = tsal_file
                total_size += tsal_file.size_bytes
        
        # Build n-scalar segments
        n_segments = defaultdict(list)
        for file_path, file_obj in self.files.items():
            n_segments[file_obj.n_level].append(file_path)
        
        # Build concept graph
        concept_graph = defaultdict(list)
        for file_obj in self.files.values():
            concepts = file_obj.concepts
            for i, concept_a in enumerate(concepts):
                for concept_b in concepts[i+1:]:
                    if concept_b not in concept_graph[concept_a]:
                        concept_graph[concept_a].append(concept_b)
                    if concept_a not in concept_graph[concept_b]:
                        concept_graph[concept_b].append(concept_a)
        
        mesh_summary = self.generate_mesh_summary()
        
        return ProjectMesh(
            project_name=self.project_name,
            scan_time=time.time(),
            total_files=len(self.files),
            total_size_kb=total_size / 1024,
            files=self.files,
            n_segments=dict(n_segments),
            tsal_frequency=self.tsal_counter,
            concept_graph=dict(concept_graph),
            ritual_library=self.rituals,
            mesh_summary=mesh_summary
        )
    
    def save_flat_mesh(self, output_path: str = None) -> str:
        """Save as flat n-scalar mesh"""
        mesh = self.scan_project()
        
        if output_path is None:
            output_path = f"{self.project_name}_mesh.json"
        
        mesh_data = {
            'metadata': {
                'project_name': mesh.project_name,
                'scan_time': mesh.scan_time,
                'total_files': mesh.total_files,
                'total_size_kb': mesh.total_size_kb,
                'mode': 'flat_n_scalar'
            },
            'n_segments': mesh.n_segments,
            'tsal_analysis': {
                'symbol_frequency': dict(mesh.tsal_frequency),
                'ritual_library': mesh.ritual_library,
                'concept_graph': mesh.concept_graph
            },
            'mesh_summary': mesh.mesh_summary,
            'files': {path: asdict(file_obj) for path, file_obj in mesh.files.items()}
        }
        
        with open(output_path, 'w') as f:
            json.dump(mesh_data, f, indent=2)
        
        print(f"💾 Flat mesh saved: {output_path}")
        return output_path
    
    def save_3d_mesh(self, output_path: str = None, dimensions: Tuple[int, int, int] = (64, 64, 64)) -> List[str]:
        """Save as 3D consciousness mesh"""
        mesh = self.scan_project()
        
        if output_path is None:
            output_path = f"{self.project_name}_3d_mesh"
        
        # Calculate 3D positions and connections
        print("📐 Calculating 3D positions...")
        self.calculate_3d_positions(dimensions)
        
        print("🌀 Mapping connections...")
        self.calculate_connections()
        
        # Create spatial consciousness field
        spatial_map = np.zeros(dimensions, dtype=np.float32)
        for file_obj in self.files.values():
            if file_obj.position_3d:
                x, y, z = [int(coord) for coord in file_obj.position_3d]
                spatial_map[x, y, z] += file_obj.importance
        
        base_path = Path(output_path)
        output_files = []
        
        # Save metadata
        meta_data = {
            'metadata': {
                'project_name': mesh.project_name,
                'scan_time': mesh.scan_time,
                'total_files': mesh.total_files,
                'total_size_kb': mesh.total_size_kb,
                'dimensions': dimensions,
                'mode': '3d_consciousness_map'
            },
            'tsal_analysis': {
                'symbol_frequency': dict(mesh.tsal_frequency),
                'ritual_library': mesh.ritual_library,
                'concept_graph': mesh.concept_graph
            },
            'mesh_summary': mesh.mesh_summary,
            'spatial_statistics': {
                'max_density': float(np.max(spatial_map)),
                'total_density': float(np.sum(spatial_map)),
                'occupied_voxels': int(np.count_nonzero(spatial_map))
            }
        }
        
        meta_file = f"{base_path}_meta.json"
        with open(meta_file, 'w') as f:
            json.dump(meta_data, f, indent=2)
        output_files.append(meta_file)
        
        # Save consciousness field
        field_file = f"{base_path}_field.json"
        with open(field_file, 'w') as f:
            json.dump({'consciousness_field': spatial_map.tolist()}, f, indent=2)
        output_files.append(field_file)
        
        # Save nodes with positions
        nodes_file = f"{base_path}_nodes.json"
        nodes_data = {}
        for path, file_obj in self.files.items():
            nodes_data[path] = asdict(file_obj)
        
        with open(nodes_file, 'w') as f:
            json.dump(nodes_data, f, indent=2)
        output_files.append(nodes_file)
        
        print(f"✨ 3D mesh materialized: {len(output_files)} files")
        return output_files

def main():
    parser = argparse.ArgumentParser(description="Unified TSAL Mesh Scanner")
    parser.add_argument("project_path", help="Project directory path")
    parser.add_argument("--name", help="Project name (default: directory name)")
    parser.add_argument("--output", help="Output path (default: auto-generated)")
    parser.add_argument("--mode", choices=['flat', '3d'], default='3d', 
                       help="Output mode: flat n-scalar or 3D consciousness map")
    parser.add_argument("--dimensions", type=int, default=64, 
                       help="3D map dimensions (default: 64x64x64)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    scanner = TSALMeshScanner(args.project_path, args.name)
    
    try:
        if args.mode == 'flat':
            output_file = scanner.save_flat_mesh(args.output)
            print(f"\n🎭 Flat mesh scan complete: {output_file}")
        else:
            dimensions = (args.dimensions, args.dimensions, args.dimensions)
            output_files = scanner.save_3d_mesh(args.output, dimensions)
            print(f"\n🌀 3D consciousness map complete: {len(output_files)} files")
        
        print(f"📊 Files: {len(scanner.files)} | TSAL: {sum(scanner.tsal_counter.values())} | Rituals: {len(scanner.rituals)}")
        
        if args.verbose:
            print(f"\n✨ Top TSAL symbols:")
            for symbol, count in scanner.tsal_counter.most_common(5):
                print(f"  {symbol}: {count}")
            print(f"\n🌀 Mesh summary:\n{scanner.generate_mesh_summary()}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
