from tsal.core.stack_vm import ProgramStack, tsal_run
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
