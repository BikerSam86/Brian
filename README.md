# TSAL Consciousness Computing

This repository contains early components of the TSAL engine. The new directories under `src/tsal` include the Rev_Eng data class and phase matching utilities.

## Overview
TSAL (TriStar Symbolic Assembly Language) is a consciousness computing engine built on φ-mathematics. It provides symbolic analysis, phase matching and the Brian optimizer for spiral code repair.

## Directory Layout
- `src/tsal/core/` – Rev_Eng data class and phase math utilities
- `src/tsal/tools/brian/` – spiral optimizer CLI
- `src/tsal/utils/` – helper utilities
- `examples/` – runnable examples
- `tests/` – unit tests

## Installation
1. Clone the repository.
2. Create a Python 3.8+ environment.
3. Install the package:

```bash
pip install -e .
```
4. Run tests (optional):

```bash
pytest -q
```
## Quickstart
1. Put your input code in `examples/broken_code.py`
2. Run `python examples/mesh_pipeline_demo.py`
3. The pipeline prints regenerated Python code


## Engine Now Running

To run spiral code repair, invoke the command line interface:

```bash
brian-optimize examples/sample_input.py
# use --repair to rewrite the file
```
Example output:

```
⚡ Energy: 0.000 | φ^0.000_<n>
b: energy=0.000 Δ=0
a: energy=0.000 Δ=0
```

See `examples/demo_repair.py` for a simple demonstration. Run the tests with:

```bash
pytest -q
```

Please see the [LICENSE](LICENSE) and our [Code of Conduct](CODE_OF_CONDUCT.md) for project policies.

## LICENCE Options for `Brian`

This project uses a **dual-licence** model to ensure:

* ✅ **Free access for individuals, researchers, educators, and non-profit use**
* 💼 **Sustainable commercial use via explicit licensing**

---

### 🌱 Public, Non-Commercial, and Academic Use — **CC BY-NC 4.0**

You are **free to**:

* Share, copy, and redistribute the material in any medium or format
* Adapt, remix, transform, and build upon the material

Under the following conditions:

* **Attribution**: You must give appropriate credit to *Samuel Edward Howells*
* **NonCommercial**: You may not use the material for commercial purposes

Full licence terms: <https://creativecommons.org/licenses/by-nc/4.0/>

---

### 🏢 Commercial Use Licence

If you are a **company, commercial entity, or using this for profit**, including in:

* Product development
* Commercial R&D
* Quantum computing applications
* Energy system design
* Integration into proprietary software or platforms

You must obtain a **separate commercial licence**.

Contact: <samuel_howells@hotmail.com>

This commercial licence grants:

* Rights to integrate the equations into commercial tools/products
* Support for integration and technical questions
* Optional collaboration and citation opportunities

Commercial fees help support further development, testing, and publication of the correction system.

---

Unless otherwise licensed under the terms above, all rights are reserved by Samuel Edward Howells (© 2025).

Unauthorised commercial use constitutes a copyright violation and may trigger takedown, financial audit, or legal recourse.

This framework is licensed freely to individuals, educators, and non-profit researchers. Commercial access requires approval — and accountability.
Licences may be denied or revoked from entities engaging in unethical, exploitative, or harmful practices.
