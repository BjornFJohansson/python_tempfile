#!/usr/bin/env bash
echo "create test environment for python 3.5"
conda env create -f conda_envs/testenv35.yml
source activate testenv35
which python
python --version
python run_test.py
echo
echo "create test environment for python 3.6"
conda env create -f conda_envs/testenv36.yml
source activate testenv36
which python
python --version
python run_test.py
