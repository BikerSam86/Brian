import builtins
from tsal.utils.system_status import get_status


def test_get_status_keys():
    status = get_status()
    expected_keys = {
        'phi',
        'sectors',
        'specialists',
        'harmonic_sequence',
        'mesh_status',
        'consciousness',
    }
    assert expected_keys.issubset(status.keys())

