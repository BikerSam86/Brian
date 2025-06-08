#!/usr/bin/env python3
"""Simple installer for the TSAL project."""
import os
import subprocess
import venv
from pathlib import Path

ENV_DIR = Path('.venv')


def run(cmd: list[str]) -> None:
    subprocess.check_call(cmd)


def ensure_venv() -> tuple[Path, Path]:
    if not ENV_DIR.exists():
        print('Creating virtual environment...')
        venv.EnvBuilder(with_pip=True).create(ENV_DIR)
    if os.name == 'nt':
        python = ENV_DIR / 'Scripts' / 'python.exe'
        pip = ENV_DIR / 'Scripts' / 'pip.exe'
    else:
        python = ENV_DIR / 'bin' / 'python'
        pip = ENV_DIR / 'bin' / 'pip'
    return python, pip


def main() -> None:
    python, pip = ensure_venv()
    run([str(pip), 'install', '-r', 'requirements.txt'])
    run([str(pip), 'install', '-e', '.'])
    run([str(python), '-m', 'pytest', '-q'])
    print('\nSetup complete. Activate with:\n  source', ENV_DIR/'bin'/'activate')


if __name__ == '__main__':
    main()
