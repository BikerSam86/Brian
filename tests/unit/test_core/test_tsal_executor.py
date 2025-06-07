from tsal.core.tsal_executor import TSALExecutor, TSALOp, SpiralVector


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
