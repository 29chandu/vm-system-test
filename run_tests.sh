#!/bin/sh
python3.10 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python -m pytest --alluredir=/home/chandra/chandra/jenkins/allure-report --html=report.html --self-contained-html
