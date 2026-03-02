def areBracketsProperlyMatched(code_snippet):
    mapr = {'}': '{', ']': '[', ')': '('}
    stk = []
    for c in code_snippet:
        if c in ['(', '[', '{']:
            stk.append(c)
        elif c in mapr:
            if not stk or mapr[c] != stk.pop():
                return False
    return not stk

if __name__ == '__main__':
    print(areBracketsProperlyMatched('(da)()))s(){[df]}'))
    print(areBracketsProperlyMatched('(da)()s(){[df]}'))
    print(areBracketsProperlyMatched('{{(()'))
