#!/bin/bash

pyinstaller --onefile --hidden-import=pyxhook --hidden-import=urllib3 --hidden-import=requests --hidden-import=base64 smashlog.py
