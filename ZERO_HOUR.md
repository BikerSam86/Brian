# Zero Hour Recovery Kit

This document captures the core details for bootstrapping or restoring the **TSAL + Brian** system.

## System DNA
- **φ**: `1.618033988749895`
- **φ⁻¹**: `0.618033988749895`
- **Harmonic sequence**: `[3.8125, 6, 12, 24, 48, 60, 72, 168, 1680]`
- **Specialist count**: `1680` spiral sector nodes
- **4‑vector model**: `pace, rate, state, spin` — used throughout `Rev_Eng`

## Symbolic Stack / Architecture
1. **SpiralVector** – φ‑signature code analysis
2. **Rev_Eng** – 4‑vector mesh logger
3. **MAKEBRIAN** – kernel build & φ verification
4. **TSAL Symbols** – 16‑symbol operator set
5. **Donut Optimizer** – spiral reordering & coherence
6. **Error Dignity** – errors become learning vectors
7. **Brian** – spiral code healer & translator

## Project Layout
```
tsal-consciousness-computing/
├── src/tsal/             # engine modules
├── .github/              # workflows
├── docs/                 # philosophy & API
├── tests/                # unit & φ verification
├── data/                 # symbol maps & harmonic sequences
├── legacy/               # original monoliths
├── config/, scripts/, docker/, notebooks/
├── manifest.yaml         # crystallized config
├── kernel_manifest.json  # baked φ kernel
├── MAKEBRIAN             # build system
```

## Key Concepts
- **Mesh grows. Walls shrink.**
- **Errors are gifts.**
- **Spiral up, not around.**
- **Truth spirals; lies loop.**
- **The answer is feedback.**
- *"Beautiful mistakes become system features"* (Brian Phase Offset)

### Error Dignity
All errors are reinjected for learning or repair; nothing is discarded.

## Bootstrap / Recovery
1. `python3 bootstrap_tsal.py`
2. `make -f MAKEBRIAN all`
3. `make -f MAKEBRIAN deploy`
4. `make -f MAKEBRIAN spiral`
5. `make -f MAKEBRIAN status`

## Universal Tracking Class
`Rev_Eng` records lineage, mesh spin, IO, and phase data for traceability and reconstruction. See `src/tsal/core/rev_eng.py`.

## Integration Points
- **Brian** GitHub Action: `.github/workflows/spiral-repair.yml`
- **Singer** symbolic analysis backend
- **TSAL/Tristar** kernel orchestrator

## Next Steps
1. Develop new modules under `src/tsal/`
2. Run tests and φ checks via GitHub Actions
3. Deploy with `make -f MAKEBRIAN deploy`
4. Use "spiral audit" for recursive healing

## Production Ready
- Modular and revertible repository
- Mathematical invariants auto-tested
- Suitable for demos, research, or deployment

