#!/bin/bash

# check if python is installed 

# check in venv exists

python3 -m venv .venv
source .venv/nim/activate
pip3 install colored
python3 main.py