#!/usr/bin/env python3
import sys
from cx_Freeze import setup,Executable
base=''
if sys.platform=='win32':
    base="Win32GUI"
setup(
    name='zerojudge.exe',
    version='3.6.6',
    description='zerojudge in command line',
    executables=[Executable("zerojudge-cli.py",base=base)]
)
