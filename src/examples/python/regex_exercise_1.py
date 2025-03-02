#!/usr/bin/env python
from __future__ import print_function

import sys
import re

if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "FILE")
    exit()

filename = sys.argv[1]
f = open(filename, 'r')

for line in f:
    print(line, end=" ")

    match = re.search(r'REGEX1', line)
    if match:
       print("   Matching 1", match.group(0))

    match = re.search(r'REGEX2', line)
    if match:
       print("   Matching 2", match.group(0))
