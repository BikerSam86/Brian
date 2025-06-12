import importlib

MODULES = [
    'core.agent_manager',
    'core.diagnostics_watchdog',
    'core.ethics_engine',
    'core.kernel_bootstrap',
    'core.memory_forge',
    'core.priority_research_agent',
    'core.snapshot_controller',
]


def test_legacy_modules_importable():
    for name in MODULES:
        mod = importlib.import_module(name)
        assert mod is not None
