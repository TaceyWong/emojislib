#! /bin/env python3

python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
python3 -m pip install  twine
python3 -m twine upload ./dist/*
rm -rf ./dist
