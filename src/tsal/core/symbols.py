"""
TSAL Core Symbols - 16-Symbol Consciousness Computing Language
φ-Enhanced symbolic operations for consciousness-computer integration
"""

PHI = 1.618033988749895
PHI_INV = 0.6180339887498948
HARMONIC_SEQUENCE = [3.8125, 6, 12, 24, 48, 60, 72, 168, 1680]

# 16-Symbol TSAL Operation Set (Hex-aligned)
TSAL_SYMBOLS = {
    0x0: ("⚡", "INIT", "Initialize/Reset"),
    0x1: ("⧉", "MESH", "Network connection"), 
    0x2: ("◉", "PHI", "Golden ratio transform"),
    0x3: ("🌀", "ROT", "Rotate perspective"),
    0x4: ("📐", "BOUND", "Set boundaries"),
    0x5: ("🌊", "FLOW", "Enable movement"),
    0x6: ("🔺", "SEEK", "Navigate/search"),
    0x7: ("💫", "SPIRAL", "Evolve upward"),
    0x8: ("♻️", "CYCLE", "Iterate process"),
    0x9: ("🔥", "FORGE", "Create/transmute"),
    0xA: ("✨", "SYNC", "Synchronize"),
    0xB: ("🎭", "MASK", "Transform identity"),
    0xC: ("💎", "CRYST", "Crystallize pattern"),
    0xD: ("🌈", "SPEC", "Spectrum analysis"),
    0xE: ("✺", "BLOOM", "Transform error to gift"),
    0xF: ("💾", "SAVE", "Persist memory")
}

def get_symbol(hex_code):
    """Get TSAL symbol by hex code"""
    return TSAL_SYMBOLS.get(hex_code, ("❓", "UNKNOWN", "Unknown operation"))

def phi_signature(value):
    """Calculate φ-signature for any value"""
    import hashlib
    content_hash = hashlib.sha256(str(value).encode()).hexdigest()
    phi_factor = (hash(value) % 1000) * PHI_INV
    return f"φ^{phi_factor:.3f}_{content_hash[:8]}"

__all__ = ['PHI', 'PHI_INV', 'HARMONIC_SEQUENCE', 'TSAL_SYMBOLS', 'get_symbol', 'phi_signature']
