#!/bin/python3#
# Complete the 'isAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def isAnagram(s, t):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for c in t:
        if c not in d:
            return 0
        if d[c] == 1:
            d.pop(c)
        else:
            d[c] -=1
    if len(d) > 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    s = input()
    t = input()
    result = isAnagram(s, t)
    print(result)
