"""Compatibility shim pointing to the main TSAL package."""

from tsal import __all__ as _all
import tsal as _tsal

globals().update({name: getattr(_tsal, name) for name in _all})

__all__ = list(_all)
