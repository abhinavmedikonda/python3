#!/bin/python3
#
# Complete the 'generateAngleBracketSequences' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER n as parameter.
#

def generateAngleBracketSequences(n):
    return recur(list(), str(), n, 0)

def recur(s_, s, n, z):
    if n==0 and z==0:
        return s_.append(s)
    if n>0:
        recur(s_, s+'<', n-1, z+1)
    if z>0:
        recur(s_, s+'>', n, z-1)
    return s_

if __name__ == '__main__':
    n = int(input().strip())
    result = generateAngleBracketSequences(n)
    print('\n'.join(result))
