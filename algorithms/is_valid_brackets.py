#!/bin/python3
#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

def areBracketsProperlyMatched(code_snippet):
    ht = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for c in code_snippet:
        if c not in ['(', '[', '{', ')', ']', '}']:
            continue
        if c in ['(', '[', '{']:
            stack.append(c)
        elif len(stack) == 0 or c != ht[stack.pop()]:
            return 0
    return 1

if __name__ == '__main__':
    code_snippet = input()
    result = areBracketsProperlyMatched(code_snippet)
    print(int(result))
