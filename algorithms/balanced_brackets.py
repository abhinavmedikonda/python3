def is_balanced(code_snippet):
    stak = []
    mapr = {')': '(', '}': '{', ']': '['}
    opng = {'(', '{', '['}
    for v in code_snippet:
        if v in opng:
            stak.append(v)
        elif not stak or mapr[v] != stak.pop():
            return False
    return not stak

if __name__ == '__main__':
    print(is_balanced('()()))(){[]}'))
    print(is_balanced('()()(){[]}'))
    print(is_balanced('{{(()'))
