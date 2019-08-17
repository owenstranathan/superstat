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

# TODO: look for .superstatpaths in more places

import os
import subprocess
from pathlib import Path
from typing import List
from argparse import ArgumentParser

cwd = os.getcwd()
runtimepath = Path(os.path.dirname(__file__))
pathsfile = runtimepath / ".superstatpaths"


def is_child(path1, path2):
    try:
        return bool(path1.relative_to(path2))
    except ValueError:
        return False

def matches(path1, pathpattern):
    return True

def stat_dir(directory):
    if not Path(directory).exists():
        print(" %s: No such directory" % directory)
        return
    proc = subprocess.run(["git", "status", "--short"], capture_output=True, cwd=directory, shell=True)
    if proc.stdout:
        print(" %s" % directory)
        for line in proc.stdout.decode().split("\n"):
            print("\t%s" % line)

def main():
    pathpatterns = []
    if (pathsfile.exists):
        for pattern in pathsfile.open("r").read(). split('\n'):
            if pattern.strip().startswith("#"):
                continue
            if pattern:
                pathpatterns.append(pattern)
    if not pathpatterns:
        pathpatterns = [cwd + "*"]  # If there are no settings then just look everywhere
    for pattern in pathpatterns:
        if pattern.endswith("*"):
            for path in Path(pattern).parent.glob("**/.git"):
                if path.is_dir():
                    stat_dir(str(path.parent))
        else:
            stat_dir(pattern)

if __name__ == "__main__":
    parser = ArgumentParser(description="Stat all the git repos you care about at once")
    parser.add_argument("-e", "--edit", nargs='?', const="vim", default=None, help="Edit .superstatpaths with program given by [EDIT] or vim default")
    parser.add_argument("-w", "--where", action="store_true", help="Where is .superstatpaths")
    parser.add_argument("-s", "--show", action="store_true", help="What's in .superstatpaths")
    args = parser.parse_args();
    if args.edit:
        os.system("%s %s" % ( args.edit, pathsfile))
        print(args.edit)
    elif args.where:
        print("\n")
        print("\t%s" % pathsfile)
    elif args.show:
        with pathsfile.open("r") as inf:
            print("\n")
            for path in inf.read().split("\n"):
                print("\t%s" % path)
    else:
        main()
