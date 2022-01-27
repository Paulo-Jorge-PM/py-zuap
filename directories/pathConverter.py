#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path, PureWindowsPath

#You can even use pathlib to explicitly convert a Unix path into a Windows-formatted path:

filename = Path("source_data/text_files/raw_data.txt")

# Convert path to Windows format
path_on_windows = PureWindowsPath(filename)

print(path_on_windows)
# prints "source_data\text_files\raw_data.txt"