#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'hasCircularDependency' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY dependencies
#

def hasCircularDependency(n, dependencies):
    if len(dependencies) == 0:
        return 0
    hsh = dict()
    for item in dependencies:
        if item[0] == item[1]:
            return 1
        if item[0] not in hsh:
            hsh[item[0]] = set()
        hsh[item[0]].add(item[1])

    def is_cycle(r, stk, v, hsh):
        if r in stk:
            return True
        if r in v:
            return False
        stk.add(r)
        v.add(r)
        for i in hsh[r]:
            if is_cycle(i, stk, hsh):
                return True
        stk.remove(r)
        return False
        
    return 1 if is_cycle(next(iter(hsh)), set(), set(), hsh) else 0

if __name__ == '__main__':
    n = int(input().strip())

    dependencies_rows = int(input().strip())
    dependencies_columns = int(input().strip())

    dependencies = []

    for _ in range(dependencies_rows):
        dependencies.append(list(map(int, input().rstrip().split())))

    result = hasCircularDependency(n, dependencies)

    print(int(result))
