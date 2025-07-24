#!/usr/bin/env bash
set -e
sudo apt-get update
sudo apt-get install -y build-essential python3-venv git curl
python3 installer.py
