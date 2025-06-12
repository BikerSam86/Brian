from fastapi.testclient import TestClient
from tsal.api import app

client = TestClient(app)

def test_optimize_spiral():
    resp = client.post('/optimize_spiral', json={'code': 'def x():\n    return 1'})
    assert resp.status_code == 200
    body = resp.json()
    assert 'repaired_code' in body
    assert 'symbolic_log' in body

def test_spiral_score():
    resp = client.post('/spiral_score', json={'code': 'x=1'})
    assert resp.status_code == 200
    body = resp.json()
    assert 'phi_alignment' in body
    assert 'spiral_score' in body
