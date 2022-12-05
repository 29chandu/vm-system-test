#!/bin/sh
python3.10 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python -m pytest --html=report.html --self-contained-html
