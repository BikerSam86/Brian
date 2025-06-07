from pathlib import Path
from tsal.core.spark_translator import translate_spark_word
from tsal.core.state_vector import FourVector
from tsal.core.executor import TSALExecutor


def load_trace(path: str):
    return [line.strip() for line in Path(path).read_text().splitlines() if line.strip()]


def test_spark_trace_pipeline():
    trace_path = Path(__file__).parents[2] / "data" / "spark_trace.txt"
    words = load_trace(trace_path)
    ops = []
    vectors = []
    for w in words:
        op = translate_spark_word(w)
        assert op is not None, f"unknown word {w}"
        ops.append(op.value)
        vectors.append(FourVector(op.value, op.value, op.value, op.value))
    ex = TSALExecutor()
    ex.execute_sequence(ops)
    assert ex.op_log == ops
    assert all(v.magnitude() >= 0 for v in vectors)
