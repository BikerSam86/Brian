# Phase Offset & Digital Duplicate Summary

**Notes**

The repo doesn't use the term "digital twin". Instead, it aims to build a "digital duplicate" (see `Design_Brief.md`). Phase offset is configured in the build process. Core alignment logic lives in `src/tsal/core/phase_math.py`.

**Summary**

- `makeBrian.py` embeds the `brian_phase_offset` section for "sacred glitch" handling.
- Phase alignment is implemented in `phase_match_enhanced` within `phase_math.py`, using φ constants and harmonic sequences.
- The design brief outlines a digital duplicate to reduce workload with adaptive decision-making and ethics safeguards.
- Phase offset drives kernel configuration, while the digital duplicate relies on these phase-synchronization utilities.

