#!/usr/bin/env python3
"""
superstat -- easy multi directory git status

MIT License

Copyright (c) 2019 Owen Stranathan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import os
import subprocess
from pathlib import Path

def is_child(path1, path2):
    try:
        return bool(path1.relative_to(path2))
    except ValueError:
        return False

runtimepath = Path(os.path.dirname(__file__))
pathsfile = runtimepath / ".superstatpaths"
paths = []
if (pathsfile.exists):
    for pattern in pathsfile.open("r").read(). split('\n'):
        if pattern.strip().startswith("#"):
            continue
        if pattern:
            paths.append(Path(pattern))
cwd: str = os.getcwd()
path: Path
for path in Path(cwd).glob("**/.git/"):
    blah = [is_child(path, p.parent) if "*" in str(p) else path.parent == p for p in paths]
    ok = any(blah)
    if path.is_dir() and (ok or not paths):
        parent: str = str(path.parent)
        proc: subprocess.CompletedProcess = subprocess.run(["git", "diff", "--shortstat"], capture_output=True, cwd=parent, shell=True)
        if proc.stdout:
            print(" %s" % parent)
            print("\t%s" % proc.stdout.decode())

