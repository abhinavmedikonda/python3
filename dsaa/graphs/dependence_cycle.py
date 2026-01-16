def has_circular_dependency(n, dependencies):
    hsh = dict()
    for item in dependencies:
        if item[0] == item[1]:
            return 1
        if item[0] not in hsh:
            hsh[item[0]] = set()
        hsh[item[0]].add(item[1])
        if item[1] not in hsh:
            hsh[item[1]] = set()

    def is_cycle(r):
        if r in stk:
            return True
        if r in vst:
            return False
        stk.add(r)
        vst.add(r)
        for i in hsh[r]:
            if is_cycle(i):
                return True
        stk.remove(r)
        return False
    stk = set()
    vst = set()
    
    for it in hsh:
        if is_cycle(it):
            return True
        
    return False

'''
4
3
1 0
2 1
3 2
'''
if __name__ == '__main__':
    n = int(input().strip())

    dependencies_rows = int(input().strip())
    dependencies_columns = 2

    dependencies = []

    for _ in range(dependencies_rows):
        dependencies.append(list(map(int, input().rstrip().split())))

    result = has_circular_dependency(n, dependencies)

    print(int(result))
