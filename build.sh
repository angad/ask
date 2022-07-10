#!/bin/bash
pip3 install pex
cd ..
pex ask -r ask/requirements.txt -e ask:main -o ask/ask.pex
