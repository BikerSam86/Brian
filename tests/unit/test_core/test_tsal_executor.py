from tsal.core.tsal_executor import TSALExecutor, TSALOp, SpiralVector, ExecutionMode
from tsal.core.executor import MetaFlagProtocol


def test_cycle_creates_nodes():
    tvm = TSALExecutor()
    program = [
        (TSALOp.INIT, {'mesh': True}),
        (TSALOp.MESH, {}),
        (TSALOp.CYCLE, {'count': 2, 'start': 1, 'end': 2}),
    ]
    tvm.execute(program)
    assert len(tvm.mesh) == 3


def test_spiral_depth_increase():
    tvm = TSALExecutor()
    program = [
        (TSALOp.SPIRAL, {'increment': 2}),
    ]
    tvm.execute(program)
    assert tvm.spiral_depth == 2


def test_mode_trace():
    tvm = TSALExecutor(MetaFlagProtocol(narrative_mode=True))
    program = [
        (TSALOp.INIT, {'mesh': True}),
    ]
    tvm.execute(program)
    assert tvm.mode == ExecutionMode.TRACE


def test_mode_fork():
    tvm = TSALExecutor(MetaFlagProtocol(fork_tracking=True))
    program = [
        (TSALOp.FORGE, {'fork': True}),
    ]
    tvm.execute(program)
    assert tvm.mode == ExecutionMode.FORK


def test_mode_arm_on_error():
    tvm = TSALExecutor()
    tvm.error_mansion.append({'type': 'test'})
    tvm._switch_mode(0)
    assert tvm.mode == ExecutionMode.ARM
