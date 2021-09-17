#!/bin/bash

rm -rfv venv 2>/dev/null
python -m virtualenv venv
source venv/bin/activate
pip install $1
python test_import.py

