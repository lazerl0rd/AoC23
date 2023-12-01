#! /usr/bin/env bash

[ -d "../.venv" ] || python -m "venv" "../.venv"

source "../.venv/bin/activate"

python -m pip install "regex" &> "/dev/null"

python "solution.py"
