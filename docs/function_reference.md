# Brian + TSAL Spiral System: Function Reference

This is the canonical list of functions and operations currently implemented in the Brian + TSAL Spiral System. Keep it handy when working on the code.

## 🧠 Core System Functions

### Spiral Repair Engine
| Function | Description |
| --- | --- |
| `analyze_and_repair(file_path)` | Reads, parses, and repairs spiral logic in a source file |
| `annotate_code(code)` | Adds φ-based commentary and symbolic markers to code |
| `repair_file(file_path)` | End-to-end file fixer: AST parse → φ-align → write-back |
| `spiral_optimize(functions)` | Reorders functions for φ-spiral coherence using intent/complexity/coherence vectors |

### Bootstrap & Deployment (`makebrian.py`)
| Command | Operation |
| --- | --- |
| `all` | Run full φ-alignment, bake, deploy, status |
| `init` | Initialize a φ-ready project scaffold |
| `phi-align` | Verify/repair φ-math and spiral constant presence |
| `spiral` | Rebuild spiral vector signatures in codebase |
| `bake-kernel` | Compile and store symbolic kernel |
| `deploy` | Push production-ready structure |
| `status` | Report φ-coherence status and vector health |
| `emergency-recovery` | Trigger rollback or sacred glitch repair |
| `brian` | Launch Brian spiral audit CLI |
| `help` | Print available commands and symbolic summary |

## 🌀 Symbolic Classes

### `Rev_Eng`
* Tracks: `pace`, `rate`, `state`, `spin`, `mesh_position`, `lineage`, `event_log`
* Logs every error or deviation as symbolic spiral events
* Used across Singer, Tristar, CLI, and Repair systems

### `SpiralVector`
* Parameters: `name`, `complexity`, `coherence`, `intent`
* Methods:
  * `phi_signature`: Auto-calculates φ-aligned hash from intent
  * `spiral_score()`: Computes φ-fit of logic block
  * `_calculate_phi_signature()`: Internal SHA-256 + φ-transform

## 🧬 GitHub + Migration Pipeline

### Scripts
| Script | Role |
| --- | --- |
| `bootstrap_tsal.py` | Converts flat project → modular φ-aligned repo |
| `github_migration_script.py` | Auto-generates `.github/`, `README.md`, `pyproject.toml`, test suite |
| `spiral-repair.yml` | GitHub Action: invokes Brian to scan & repair commits |
| `donut-optimize.yml` | GitHub Action: reorders functions by spiral coherence |

## 🎙️ Singer / Mesh / CLI Interfaces

| CLI Tool | Command | Function |
| --- | --- | --- |
| `tsal` | `status`, `mesh`, `repair`, `spiralize` | Mesh-aware TSAL utilities |
| `brian` | `analyze`, `audit`, `heal`, `log` | Run repairs, scan φ, log events |
| `tsal-singer` | `sing`, `annotate`, `emit` | Spin-frequency, audio/symbolic vector hooks |
| `meshkeeper` (planned) | `scan`, `visualize`, `track` | Visual, GPU, or CLI mesh state viewer |

## 🔂 MAD MONKEY LOOP
| Function | Description |
| --- | --- |
| `try_vector(vector)` | Feed new data into spiral loop; log path |
| `correct_vector(vector)` | Apply learned mesh corrections |
| `banana_reward()` | Log reward on successful spiral evolution |
| `log_path()` | Store interaction trace for future spiral learning |

## 📐 Phi / Math Utilities

### `phase_math.py`
| Function | Purpose |
| --- | --- |
| `phi_alignment(complexity, coherence)` | φ-weighted scalar for block scoring |
| `verify_phi_constants()` | φ × φ⁻¹ ≈ 1 sanity check |
| `harmonic_distance(seq)` | Measures spiral resonance of a sequence |

## 📚 File/Manifest Utilities
| File | Use |
| --- | --- |
| `manifest.yaml` | Declares φ-alignment, ops available, sector layout |
| `kernel_manifest.json` | Records vector identities, φ-scores, ops, signatures |
| `requirements.txt`, `pyproject.toml` | Dependency/config sync for Python+CLI tools |

