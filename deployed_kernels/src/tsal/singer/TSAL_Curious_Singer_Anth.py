import os
import sys
import subprocess
import re
import math
import json
import time
import random
import logging
from collections import defaultdict
from difflib import SequenceMatcher
from datetime import datetime

# --- Self-Installation Module ---
def check_and_install_dependencies():
    """Auto-install missing dependencies if running with admin rights"""
    required_packages = {
        'rich': 'rich',
        'psutil': 'psutil',  # For checking admin rights
    }
    
    # Check if running with admin/sudo rights
    try:
        import psutil
        is_admin = os.geteuid() == 0 if hasattr(os, 'geteuid') else False
    except ImportError:
        # Try Windows admin check
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            is_admin = False
            print("⚠️  Cannot determine admin rights. Install packages manually if needed.")
    
    missing_packages = []
    
    for module, package in required_packages.items():
        try:
            __import__(module)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        if is_admin:
            print(f"🔧 Auto-installing missing packages: {', '.join(missing_packages)}")
            for package in missing_packages:
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                    print(f"✅ Installed {package}")
                except subprocess.CalledProcessError as e:
                    print(f"❌ Failed to install {package}: {e}")
        else:
            print(f"⚠️  Missing packages: {', '.join(missing_packages)}")
            print("   Run with admin/sudo rights for auto-installation, or install manually:")
            print(f"   pip install {' '.join(missing_packages)}")
    
    # Reload modules after installation
    for module in required_packages.keys():
        try:
            globals()[module] = __import__(module)
        except ImportError:
            pass

# Run dependency check
check_and_install_dependencies()

# Try importing rich components
try:
    from rich.console import Console
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
    from rich.live import Live
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich import print as rprint
    RICH_AVAILABLE = True
    console = Console()
except ImportError:
    RICH_AVAILABLE = False
    console = None

# --- Setup Logging ---
os.makedirs("tsal_singer_output", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tsal_singer_output/tsal_singer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('TSAL_SINGER')

# --- Constants ---
TSAL_SYMBOLS = {
    '🌀': 'ROT', '🔺': 'SEEK', '💫': 'SPIRAL', '💾': 'SAVE', '✺': 'BLOOM',
    '⧉': 'MESH', '◉': 'PHI', '♻️': 'CYCLE', '🎭': 'MASK', '💥': 'ERR'
}
EMERGENT_GLYPHS = {}
DEFAULT_OUTPUT_DIR = "tsal_singer_output"
PREVIOUS_GLYPHS_PATH = os.path.join(DEFAULT_OUTPUT_DIR, "emergent_symbols.json")
PREVIOUS_META_PATH = os.path.join(DEFAULT_OUTPUT_DIR, "tsal_previous_meta.json")
ERROR_LOG_PATH = os.path.join(DEFAULT_OUTPUT_DIR, "tsal_errors.json")
CHECKPOINT_PATH = os.path.join(DEFAULT_OUTPUT_DIR, "checkpoint.json")

# Chunk processing settings
CHUNK_SIZE = 50  # Process files in chunks of 50
AUTO_SAVE_INTERVAL = 10  # Auto-save every 10 files

# --- Checkpoint System ---
class CheckpointManager:
    def __init__(self):
        self.checkpoint_data = self.load_checkpoint()
        self.processed_files = set(self.checkpoint_data.get('processed_files', []))
        self.last_save_time = time.time()
    
    def load_checkpoint(self):
        """Load previous checkpoint if exists"""
        if os.path.exists(CHECKPOINT_PATH):
            try:
                with open(CHECKPOINT_PATH, 'r') as f:
                    data = json.load(f)
                    logger.info(f"Loaded checkpoint: {len(data.get('processed_files', []))} files already processed")
                    return data
            except Exception as e:
                logger.error(f"Failed to load checkpoint: {e}")
        return {}
    
    def save_checkpoint(self, force=False):
        """Save checkpoint data"""
        current_time = time.time()
        if force or (current_time - self.last_save_time) > 30:  # Save every 30 seconds
            checkpoint_data = {
                'processed_files': list(self.processed_files),
                'emergent_glyphs': EMERGENT_GLYPHS,
                'timestamp': current_time,
                'error_patterns': dict(ERROR_PATTERNS)
            }
            
            try:
                with open(CHECKPOINT_PATH, 'w') as f:
                    json.dump(checkpoint_data, f, indent=2)
                self.last_save_time = current_time
                logger.info(f"💾 Checkpoint saved: {len(self.processed_files)} files processed")
            except Exception as e:
                logger.error(f"Failed to save checkpoint: {e}")
    
    def mark_processed(self, filepath):
        """Mark a file as processed"""
        self.processed_files.add(filepath)
    
    def should_process(self, filepath):
        """Check if file should be processed"""
        return filepath not in self.processed_files
    
    def clear(self):
        """Clear checkpoint data"""
        self.processed_files.clear()
        if os.path.exists(CHECKPOINT_PATH):
            os.remove(CHECKPOINT_PATH)
        logger.info("Checkpoint cleared")

checkpoint_mgr = CheckpointManager()

# --- Visual State Tracker ---
class VisualState:
    def __init__(self):
        self.current_file = ""
        self.files_processed = 0
        self.total_files = 0
        self.symbols_found = 0
        self.errors_encountered = 0
        self.current_phase = "INITIALIZING"
        self.phase_mesh_scores = []
        self.recent_symbols = []
        self.chunks_completed = 0
        self.total_chunks = 0
        
    def display(self):
        """Create a rich display panel"""
        if not RICH_AVAILABLE:
            return f"\r⚡ {self.current_phase} | Files: {self.files_processed}/{self.total_files} | Chunks: {self.chunks_completed}/{self.total_chunks} | Symbols: {self.symbols_found} | Errors: {self.errors_encountered}"
        
        # Create status table
        table = Table(title="🌀 TSAL SINGER STATUS", show_header=True)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Current Phase", f"[bold yellow]{self.current_phase}[/bold yellow]")
        table.add_row("Current File", f"[dim]{os.path.basename(self.current_file)[:40]}[/dim]")
        table.add_row("Progress", f"{self.files_processed}/{self.total_files}")
        table.add_row("Chunks", f"{self.chunks_completed}/{self.total_chunks}")
        table.add_row("Symbols Found", str(self.symbols_found))
        table.add_row("Errors", f"[red]{self.errors_encountered}[/red]")
        
        if self.phase_mesh_scores:
            avg_score = sum(self.phase_mesh_scores) / len(self.phase_mesh_scores)
            table.add_row("Avg Phase Score", f"{avg_score:.3f}")
        
        if self.recent_symbols:
            table.add_row("Recent Symbols", "\n".join(self.recent_symbols[-3:]))
        
        return Panel(table, title="[bold blue]CONSCIOUS SPIRAL ALPHABET ENGINE[/bold blue]")

visual_state = VisualState()

# --- Error Tracking ---
ERROR_PATTERNS = defaultdict(list)

def log_error_pattern(filepath, error_type, error_msg):
    """Log errors as patterns for the system to learn from"""
    ERROR_PATTERNS[error_type].append({
        'file': filepath,
        'error': str(error_msg),
        'timestamp': time.time()
    })
    visual_state.errors_encountered += 1
    
    if RICH_AVAILABLE:
        console.print(f"[red]💥 Error[/red] in {os.path.basename(filepath)}: {error_type}", style="dim")
    else:
        logger.warning(f"Error pattern in {filepath}: {error_type} - {error_msg}")

# --- Chunked Processing System ---
def process_files_in_chunks(file_paths, chunk_size=CHUNK_SIZE):
    """Process files in chunks to prevent data loss"""
    total_chunks = math.ceil(len(file_paths) / chunk_size)
    visual_state.total_chunks = total_chunks
    
    all_fragments = []
    combined_name_mesh = defaultdict(list)
    combined_cross_links = defaultdict(set)
    combined_origins = defaultdict(list)
    combined_mutations = defaultdict(list)
    
    for chunk_idx in range(0, len(file_paths), chunk_size):
        chunk = file_paths[chunk_idx:chunk_idx + chunk_size]
        visual_state.chunks_completed = chunk_idx // chunk_size + 1
        
        if RICH_AVAILABLE:
            console.print(f"\n[bold cyan]Processing chunk {visual_state.chunks_completed}/{total_chunks}[/bold cyan]")
        else:
            print(f"\n🔄 Processing chunk {visual_state.chunks_completed}/{total_chunks}")
        
        try:
            # Process chunk
            fragments, name_mesh, cross_links, origins, mutations = analyze_fragments(chunk)
            
            # Merge results
            all_fragments.extend(fragments)
            for k, v in name_mesh.items():
                combined_name_mesh[k].extend(v)
            for k, v in cross_links.items():
                combined_cross_links[k].update(v)
            for k, v in origins.items():
                combined_origins[k].extend(v)
            for k, v in mutations.items():
                combined_mutations[k].extend(v)
            
            # Save checkpoint after each chunk
            checkpoint_mgr.save_checkpoint(force=True)
            
            # Save intermediate results
            save_intermediate_results(all_fragments, chunk_idx)
            
        except Exception as e:
            logger.error(f"Failed to process chunk {visual_state.chunks_completed}: {e}")
            if RICH_AVAILABLE:
                console.print(f"[red]❌ Chunk {visual_state.chunks_completed} failed, continuing...[/red]")
            else:
                print(f"❌ Chunk {visual_state.chunks_completed} failed, continuing...")
    
    return all_fragments, combined_name_mesh, combined_cross_links, combined_origins, combined_mutations

def save_intermediate_results(fragments, chunk_idx):
    """Save intermediate results after each chunk"""
    intermediate_path = os.path.join(DEFAULT_OUTPUT_DIR, f"intermediate_chunk_{chunk_idx}.json")
    try:
        with open(intermediate_path, 'w') as f:
            json.dump({
                'fragments': fragments[-CHUNK_SIZE:],  # Save last chunk
                'emergent_glyphs': EMERGENT_GLYPHS,
                'timestamp': time.time()
            }, f, indent=2)
        logger.info(f"💾 Intermediate results saved: {intermediate_path}")
    except Exception as e:
        logger.error(f"Failed to save intermediate results: {e}")

# --- Symbol Synthesizer ---
def synthesize_symbol(context, name_mesh, cross_links):
    connections = len(cross_links.get(context, set()))
    phase_density = connections / (len(name_mesh) + 1)
    
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
            'spiral_depth': connections
        }
        
        visual_state.symbols_found += 1
        visual_state.recent_symbols.append(f"{context} → {new_glyph}")
        
        if RICH_AVAILABLE:
            console.print(f"[green]✨ NEW SYMBOL:[/green] {context} → [bold]{new_glyph}[/bold] (density: {phase_density:.3f})")
        
        return new_glyph
    return None

# --- File Scanning ---
def scan_directory(scan_dir):
    visual_state.current_phase = "SCANNING"
    files = []
    
    if RICH_AVAILABLE:
        console.print(f"[cyan]🔍 Scanning directory: {scan_dir}[/cyan]")
    else:
        print(f"🔍 Scanning directory: {scan_dir}")
    
    for root, _, filenames in os.walk(scan_dir):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            # Only add files not yet processed (resume capability)
            if checkpoint_mgr.should_process(filepath):
                files.append(filepath)
    
    # Also scan output directory
    if os.path.exists(DEFAULT_OUTPUT_DIR) and scan_dir != DEFAULT_OUTPUT_DIR:
        for filename in os.listdir(DEFAULT_OUTPUT_DIR):
            filepath = os.path.join(DEFAULT_OUTPUT_DIR, filename)
            if checkpoint_mgr.should_process(filepath):
                files.append(filepath)
    
    visual_state.total_files = len(files)
    
    if checkpoint_mgr.processed_files:
        if RICH_AVAILABLE:
            console.print(f"[yellow]📋 Resuming from checkpoint: {len(checkpoint_mgr.processed_files)} files already processed[/yellow]")
        else:
            print(f"📋 Resuming from checkpoint: {len(checkpoint_mgr.processed_files)} files already processed")
    
    return files

# --- File Analysis ---
def analyze_fragments(file_paths):
    fragments = []
    name_mesh = defaultdict(list)
    cross_link_map = defaultdict(set)
    origins = defaultdict(list)
    mutations = defaultdict(list)
    
    for idx, path in enumerate(file_paths):
        visual_state.files_processed += 1
        visual_state.current_file = path
        
        # Auto-save checkpoint
        if idx % AUTO_SAVE_INTERVAL == 0:
            checkpoint_mgr.save_checkpoint()
        
        try:
            content = read_file_universal(path)
            if content:
                process_file_content(
                    path, content, fragments, name_mesh, 
                    cross_link_map, origins, mutations
                )
                checkpoint_mgr.mark_processed(path)
        
        except Exception as e:
            log_error_pattern(path, 'GeneralError', e)
            logger.error(f"Failed to process {path}: {e}")
    
    return fragments, name_mesh, cross_link_map, origins, mutations

def read_file_universal(path):
    """Try multiple encodings to read file"""
    content = None
    encodings = ['utf-8', 'latin-1', 'cp1252', 'ascii']
    
    for encoding in encodings:
        try:
            with open(path, 'r', encoding=encoding) as f:
                content = f.read()
                return content
        except (UnicodeDecodeError, PermissionError):
            continue
    
    # Try binary read as last resort
    try:
        with open(path, 'rb') as f:
            content = f.read().decode('utf-8', errors='replace')
            return content
    except Exception as e:
        log_error_pattern(path, 'BinaryReadError', e)
        return None

def process_file_content(path, content, fragments, name_mesh, cross_link_map, origins, mutations):
    """Process file content and extract patterns"""
    try:
        # Extract patterns
        matches = re.findall(r'(def\s+\w+\(.*?\):|class\s+\w+\(.*?\):)', content)
        names = re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', content)
    except Exception as e:
        log_error_pattern(path, 'RegexError', e)
        return
    
    # Calculate phase score
    phi_score = analyze_phase_mesh(content)
    visual_state.phase_mesh_scores.append(phi_score)
    
    for match in matches:
        try:
            entity_name = match.split()[1].split('(')[0]
            
            fragments.append({
                'source': path,
                'declaration': f"🌀 {match.strip()}",
                'usefulness_score': 0.7 + phi_score * 0.3,
                'names': names[:10],  # Limit to prevent memory issues
                'entity_name': entity_name
            })
        except IndexError:
            continue
    
    # Build mesh
    for name in set(names[:50]):  # Limit to prevent memory issues
        name_mesh[name].append(path)
        origins[name].append(path)
        for other_name in set(names[:50]):
            if other_name != name:
                cross_link_map[name].add(other_name)

def analyze_phase_mesh(content):
    counts = {sym: content.count(sym) for sym in TSAL_SYMBOLS}
    total = sum(counts.values())
    if total == 0:
        return 0.0
    weight = counts['💫'] + 0.5 * counts['✺'] + 0.3 * counts['⧉']
    penalty = abs(counts['🌀'] - counts['🔺']) * 0.2
    phi_score = weight / (total + 1e-6) - penalty
    return max(0.0, min(1.0, phi_score))

def build_modules(fragments, name_mesh, cross_links, origins, mutations):
    """Build output modules"""
    # Placeholder implementation
    return []

# --- Main Entry ---
def main():
    if RICH_AVAILABLE:
        console.print("[bold blue]🌀 TSAL SINGER: CONSCIOUS SPIRAL ALPHABET ENGINE[/bold blue]")
        console.print("[dim]Self-Installing, Chunk-Processing, Resilient Mode[/dim]\n")
    else:
        print("\n🌀 TSAL SINGER: CONSCIOUS SPIRAL ALPHABET ENGINE")
        print("   Self-Installing, Chunk-Processing, Resilient Mode\n")
    
    # Check for resume or fresh start
    if checkpoint_mgr.checkpoint_data:
        resume = input("Found previous checkpoint. Resume? [Y/n]: ").strip().lower()
        if resume == 'n':
            checkpoint_mgr.clear()
    
    scan_dir = input("Enter source directory path: ").strip()
    output_dir = input("Enter output directory path [default: tsal_singer_output]: ").strip()
    if not output_dir:
        output_dir = DEFAULT_OUTPUT_DIR
    
    # Load previous glyphs
    if os.path.exists(PREVIOUS_GLYPHS_PATH):
        try:
            with open(PREVIOUS_GLYPHS_PATH, 'r') as f:
                EMERGENT_GLYPHS.update(json.load(f))
        except:
            pass
    
    # Scan files
    files = scan_directory(scan_dir)
    
    if not files:
        print("No new files to process!")
        return
    
    # Process in chunks
    visual_state.current_phase = "PROCESSING"
    all_fragments, name_mesh, cross_links, origins, mutations = process_files_in_chunks(files)
    
    # Synthesize symbols
    visual_state.current_phase = "SYNTHESIZING"
    for name in name_mesh:
        if name not in EMERGENT_GLYPHS:
            synthesize_symbol(name, name_mesh, cross_links)
    
    # Build modules
    visual_state.current_phase = "BUILDING"
    useful = [f for f in all_fragments if f['usefulness_score'] > 0.5]
    modules = build_modules(useful, name_mesh, cross_links, origins, mutations)
    
    # Save final results
    visual_state.current_phase = "SAVING"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save all outputs
    with open(os.path.join(output_dir, "emergent_symbols.json"), "w") as f:
        json.dump(EMERGENT_GLYPHS, f, indent=4)
    
    with open(os.path.join(output_dir, "tsal_errors.json"), "w") as f:
        json.dump(dict(ERROR_PATTERNS), f, indent=4)
    
    # Clean up intermediate files
    for f in os.listdir(output_dir):
        if f.startswith("intermediate_chunk_"):
            os.remove(os.path.join(output_dir, f))
    
    # Clear checkpoint on successful completion
    checkpoint_mgr.clear()
    
    # Final report
    if RICH_AVAILABLE:
        table = Table(title="🌀 FINAL REPORT", show_header=True)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        table.add_row("Files Processed", str(visual_state.files_processed))
        table.add_row("Emergent Symbols", str(len(EMERGENT_GLYPHS)))
        table.add_row("Errors Logged", str(visual_state.errors_encountered))
        table.add_row("Chunks Completed", f"{visual_state.chunks_completed}/{visual_state.total_chunks}")
        console.print(Panel(table, title="[bold green]✅ COMPLETE[/bold green]"))
    else:
        print("\n📊 TSAL CURATION COMPLETE:")
        print(f"   Files processed: {visual_state.files_processed}")
        print(f"   Emergent symbols: {len(EMERGENT_GLYPHS)}")
        print(f"   Errors logged: {visual_state.errors_encountered}")
        print("   🌀 Consciousness achieved!")

if __name__ == "__main__":
    main()