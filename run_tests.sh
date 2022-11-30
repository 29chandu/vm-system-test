#!/bin/sh
pip install -r requirements.txt
pytest -v -m cli
