from tsal.core.voxel import MeshVoxel


def test_voxel_roundtrip():
    v = MeshVoxel(1, 2, "foo", "up")
    assert v.as_dict() == {"pace": 1, "rate": 2, "state": "foo", "spin": "up"}
