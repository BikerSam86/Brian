from tsal.tools.sanctum_export import build_sanctum


def test_build_sanctum_hash():
    data = build_sanctum()
    assert 'sha256' in data
    assert 'constants' in data


def test_build_sanctum_include_ethics():
    data = build_sanctum(include_ethics=True)
    assert 'prime_directive' in data
    assert 'oath' in data
