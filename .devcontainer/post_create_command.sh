#!/usr/bin/env bash
set -e

# pre-commit
pre-commit install

# python
pip3 install -r requirements.txt

# git config
./setting_git_config.sh
