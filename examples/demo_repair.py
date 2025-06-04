"""Demo script for Brian optimizer."""
from pathlib import Path
from tsal.tools.brian import optimizer

SAMPLE_FILE = Path(__file__).parent / "sample.py"

if not SAMPLE_FILE.exists():
    SAMPLE_FILE.write_text(
        """
    def b():
        return 2

    def a():
        return 1
    """
    )

print("Before:")
print(SAMPLE_FILE.read_text())
print("Suggestions:")
print("\n".join(optimizer.analyze_and_repair(str(SAMPLE_FILE))))
print("After (no changes applied):")
print(SAMPLE_FILE.read_text())
