from tsal.core.stack_vm import ProgramStack, StackVM, TensorInstruction, tsal_run
from tsal.core.tsal_executor import TSALExecutor


def test_program_stack_lifo():
    stack = ProgramStack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_tsal_run_executes_program():
    exe = tsal_run([0x0, 0x4, 0x5, 0xE])
    assert isinstance(exe, TSALExecutor)
    assert len(exe.resonance_log) == 4


def test_tensor_ops_execute():
    vm = StackVM()
    prog = [
        TensorInstruction("PUSH", [[1, 2], [3, 4]]),
        TensorInstruction("PUSH", [[5, 6], [7, 8]]),
        TensorInstruction("T_ADD"),
    ]
    result = vm.execute(prog)
    assert result[0].shape == (2, 2)
