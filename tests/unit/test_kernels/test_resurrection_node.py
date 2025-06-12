from tsal.kernels import ResurrectionNode
import asyncio

def test_rebuild_from_minimal():
    node = ResurrectionNode()
    rebuilt = asyncio.run(node.recover())
    assert rebuilt['ethos'] == 'life-first'
