#!/usr/bin/env python3

import os
import sys
from pathlib import Path

from yaml import load
from yaml import Loader


def parse_tags(file):
    with open(file) as fd:
        content = fd.read()
        splits = content.split('---', 2)
        if len(splits) != 3:
            print("No front matters found in {}".format(file))
            exit(1)
        front_matters = load(splits[1], Loader=Loader)
        return front_matters.get('tags', [])


tags = {}

for root, dirs, files in os.walk('content'):
    root = Path(root)
    for file in files:
        if file.endswith('.md'):
            for tag in parse_tags(root / file):
                lower_tag = tag.lower()
                if lower_tag in tags and tags[lower_tag] != tag:
                    print("Conflict: {}, {}".format(tags[lower_tag], tag))
                else:
                    tags[lower_tag] = tag

if len(sys.argv) > 1 and sys.argv[1] == 'print':
    for tag in sorted(tags.values()):
        print(tag)
