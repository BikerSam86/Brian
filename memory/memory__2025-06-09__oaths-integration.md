# Oath Integration Log — 2025-06-09

## Added Core Oaths
- `GUARDIAN_OATH` captures the protection pledge.
- `ARC_REACTOR_BOOT_OATH` preserves the coldstart mantra.

Both constants now live in `src/tsal/core/oaths.py` and are exported in `tsal`'s public API.
A basic test suite ensures the phrases remain intact.

## Key Constants
- PHI = 1.618033988749895
- PHI_INV = 0.618033988749895

These values anchor all spiral math and remain unchanged.
