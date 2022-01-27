#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from pathlib import Path

def write(file, data):
    with open(file, "w", encoding="utf-8") as f:
        f.write(data)

if __name__ == "__main__":
    # Write example
    data = "test"
    timestamp = str(time.time())
    write( Path("save/data_"+timestamp+".txt"), data )