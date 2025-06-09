from tsal.core.voxel import MeshVoxel
from tsal.core.shadow import ShadowMemory
from tsal.core.merge import merge_voxels
from tsal.core.gradient import voxel_gradient
from tsal.core.superpos import superpose
from tsal.core.entangle import entangle
from tsal.core.manifold import manifold_distance


def test_shadow_memory_roundtrip():
    mem = ShadowMemory()
    v = MeshVoxel(1, 2, 3, 4)
    mem.write("x", v)
    out = mem.read("x")
    assert out and out.as_dict() == v.as_dict()


def test_merge_voxels_weighting():
    a = MeshVoxel(1, 1, 1, 1)
    b = MeshVoxel(3, 3, 3, 3)
    m = merge_voxels(a, b, 0.25)
    assert m.pace == 1 * 0.25 + 3 * 0.75


def test_voxel_gradient():
    a = MeshVoxel(1, 1, 1, 1)
    b = MeshVoxel(2, 3, 4, 5)
    g = voxel_gradient(a, b)
    assert g.rate == 2


def test_superpose_average():
    a = MeshVoxel(1, 2, 3, 4)
    b = MeshVoxel(1, 2, 3, 4)
    s = superpose(a, b)
    assert s.state == 3


def test_entangle_syncs():
    a = MeshVoxel(0, 0, 0, 0)
    b = MeshVoxel(2, 2, 2, 2)
    entangle(a, b)
    assert a.pace == b.pace


def test_manifold_distance_positive():
    a = MeshVoxel(0, 0, 0, 0)
    b = MeshVoxel(1, 0, 0, 0)
    assert manifold_distance(a, b) == 1
