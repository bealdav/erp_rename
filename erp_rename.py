#!/usr/bin/env python
# coding: utf-8

import sys


def help():
    print """
This script takes an argument like this example:
    "oldname1:new1,old2:new2"
"""

QUERIES = [
    "UPDATE ir_model_data SET module = '%s' WHERE module = '%s';",
    "UPDATE ir_module_module SET name = '%s' WHERE name = '%s';",
    "UPDATE ir_module_module_dependency SET name = '%s' WHERE name = '%s';",
]


def process():
    if len(sys.argv) == 2:
        modules = sys.argv[1].split(',')
        mapping = {x[:x.find(':')]: x[x.find(':')+1:]
                   for x in modules if ':' in x}
        if not mapping:
            help()
            return True
        for old, new in mapping.items():
            for query in QUERIES:
                print query % (old, new)
    else:
        help()


if __name__ == '__main__':
    process()
