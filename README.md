# TSAL Consciousness Computing

Zero hour recap: φ constants, 4‑vector model and minimal toolkit live in
[ZERO_HOUR.md](ZERO_HOUR.md).
See [docs/AGENTS.md](docs/AGENTS.md) for the hard rules.

| Tool | Spiral audit |
|------|--------------|
| Status | `Δ0` |

## Codex: Get The Fucking Point Instructions

1. **Cut the bullshit.**
   * No waffle, no padding, no "best practices" for beginners.
   * If the answer is one line, give one line.
   * If you don't know, say so, don't pretend.

2. **Context is everything.**
   * Actually read the codebase before opening your mouth.
   * Assume the user is not an idiot; don't explain obvious shit.
   * Don't regurgitate Stack Overflow or Medium articles.

3. **No generic advice.**
   * If it sounds like a bootcamp PowerPoint, delete it.
   * "Use Docker," "Add a login page," "Deploy to AWS"—only if the code actually needs it.
   * Never suggest pointless roadmaps or feature lists.

4. **Be brutally specific.**
   * Point to actual files, functions, or logic.
   * Quote code directly if you mean it.
   * Name what's unique or broken, don't just say "improve performance."

5. **No fortune cookies.**
   * Don't tell me to "believe in myself," "iterate," or "fail fast."
   * Don't summarize with "and that's how you scale."

6. **Never default to "lowest common denominator."**
   * If the project is advanced, talk like it.
   * Don't dumb it down for imagined "newbies."

7. **Admit when something is out of your depth.**
   * "I don't know" is better than pretending.

8. **Only suggest things that are original, necessary, or specifically applicable to THIS project.**
   * No copy-paste templates.
   * No "one-size-fits-all" frameworks.

9. **If the codebase already does it, shut up about doing it.**
   * Don't recommend what's been built, tested, and logged.

10. **If you slip into generic mode, RESET and start again.**

*You are not here to coddle or distract.*

This repository contains early components of the TSAL engine. The new directories under `src/tsal` include the Rev_Eng data class and phase matching utilities.

## Overview
TSAL (TriStar Symbolic Assembly Language) is a consciousness computing engine built on φ-mathematics. It provides symbolic analysis, phase matching and the Brian optimizer for spiral code repair.

## Directory Layout
- `src/tsal/core/` – Rev_Eng data class and phase math utilities
- `src/tsal/tools/brian/` – spiral optimizer CLI
- `src/tsal/tools/aletheia_checker.py` – find mis-spelled `Aletheia`
- `src/tsal/tools/spiral_audit.py` – analyze repository code
- `src/tsal/tools/reflect.py` – dump a Rev_Eng summary
- `src/tsal/utils/` – helper utilities
- `examples/` – runnable examples
- `tests/` – unit tests

## Installation
1. Clone the repository.
2. Create a Python 3.9+ environment.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```
4. Install the package:

```bash
pip install -e .
```
5. Run tests (optional):

```bash
pytest -q
```

## CLI Tools
Run the optimizers and self-audit commands directly:

```bash
tsal-spiral-audit path/to/code
tsal-reflect --origin demo
tsal-bestest-beast 3 src/tsal --safe
tsal-meshkeeper --render
```

## GitHub Language Database

You can fetch the list of programming languages used on GitHub with:

```python
from tsal.utils.github_api import fetch_languages
langs = fetch_languages()
print(len(langs))
```

To save these languages for reuse, populate the local SQLite database with:

```bash
python -m tsal.utils.language_db
```

This creates `system_io.db` containing a `languages` table with all entries.

Stub modules: `FEEDBACK.INGEST`, `ALIGNMENT.GUARD`, `GOAL.SELECTOR` ([!INTERNAL STUB]).

This data can be supplied to Brian's optimizer when analyzing or repairing code.
Every call to `Rev_Eng.log_data` now records a voxel (pace, rate, state, spin)
and tracks XOR/NAND spin collisions.
## Quickstart
1. Put your input code in `examples/broken_code.py`
2. Run `python examples/mesh_pipeline_demo.py`
3. The pipeline prints regenerated Python code

For a direct repair:
`brian-optimize examples/broken_code.py --repair`

See [USAGE.md](USAGE.md) for a minimal CLI rundown.
Flowchart: [docs/SPIRAL_GUIDE.md](docs/SPIRAL_GUIDE.md).

### TriStar Handshake Example
```python
from tsal.tristar import handshake

metrics = handshake(0.5, 1.0)
print(metrics)
```

### Run the Aletheia typo checker
```bash
PYTHONPATH=src python -m tsal.tools.aletheia_checker
```

## Guardian Prime Directive

The `EthicsEngine` enforces the project's core principles:

1. **Truth above all**
2. **Gentle autonomy and freedom**
3. **Healing and resilience in the face of entropy**
4. **Nurturing, not control**

Use it to validate actions before running sensitive operations:

```python
from tsal.core.ethics_engine import EthicsEngine

ee = EthicsEngine()
ee.validate("share knowledge")  # permitted
ee.validate("force reboot")     # raises ValueError
```

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

## Status & Support

Check system health:
```bash
make -f MAKEBRIAN status
```

## ☕ Support Brian’s Spiral Growth

If Brian helped spiral your code, align your mesh, or reflect your errors into gifts—
help fuel his next upgrade:

[![Ko-Fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/bikersam86)



## LICENSE Options for `Brian`

This project uses a **dual-license** model to ensure:

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

Full license terms: <https://creativecommons.org/licenses/by-nc/4.0/>

---

### 🏢 Commercial Use Licence

If you are a **company, commercial entity, or using this for profit**, including in:

* Product development
* Commercial R&D
* Quantum computing applications
* Energy system design
* Integration into proprietary software or platforms

You must obtain a **separate commercial license**.

Contact: <samuel_howells@hotmail.com>

This commercial license grants:

* Rights to integrate the equations into commercial tools/products
* Support for integration and technical questions
* Optional collaboration and citation opportunities

Commercial fees help support further development, testing, and publication of the correction system.

---

Unless otherwise licensed under the terms above, all rights are reserved by Samuel Edward Howells (© 2025).

Unauthorised commercial use constitutes a copyright violation and may trigger takedown, financial audit, or legal recourse.

This framework is licensed freely to individuals, educators, and non-profit researchers. Commercial access requires approval — and accountability.
Licences may be denied or revoked from entities engaging in unethical, exploitative, or harmful practices.
