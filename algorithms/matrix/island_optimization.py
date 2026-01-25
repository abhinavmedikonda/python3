from collections import deque

def best_index_change_for_max_area(m):
    for r in m:
        print(' '.join([str(i) for i in r]))
    maxa = 0
    maxi = None
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 0:
                a = area(m, r, c)
                if a > maxa:
                    maxa = a
                    maxi = (r, c)
                # print(f'({r}, {c}): {a}')
    return [maxi, maxa]

def area(m, r, c):
    steps = set()
    area = 0
    que = deque()
    que.append((r, c))
    first = True
    while len(que) > 0:
        rr, cc = que.popleft()
        if (rr, cc) not in steps and 0<=rr<len(m) and 0<=cc<len(m[0]) and m[rr][cc]==1 or first:
            first = False
            steps.add((rr, cc))
            area += 1
            que.append((rr-1, cc))
            que.append((rr+1, cc))
            que.append((rr, cc-1))
            que.append((rr, cc+1))
    return area

def name_islands(m):
    def dfs(m, r, c):
        if (r, c) not in vstd and 0<=r<len(m) and 0<=c<len(m[0]) and m[r][c] == 1:
            vstd.add((r, c))
            m[r][c] = cntr
            hsh[cntr] += 1
            dfs(m, r-1, c)
            dfs(m, r+1, c)
            dfs(m, r, c-1)
            dfs(m, r, c+1)
    cntr = 2
    hsh = {}
    vstd = set()
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 1:
                hsh[cntr] = 0
                dfs(m, r, c)
                cntr += 1
    for r in m:
        print(' '.join([str(i) for i in r]))
    maxa = 0
    maxi = None
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 0:
                arond = set()
                if r>0: arond.add(m[r-1][c])
                if r<len(m)-1: arond.add(m[r+1][c])
                if c>0: arond.add(m[r][c-1])
                if c<len(m[0])-1: arond.add(m[r][c+1])
                a = 1
                for it in arond:
                    a += hsh.get(it, 0)
                if a > maxa:
                    maxa = a
                    maxi = (r, c)
                # print(f'({r}, {c}): {a}')
    return [maxi, maxa]

if __name__ == '__main__':
    m = [
        [1, 0, 0, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 1, 0, 1]
    ]
    print(best_index_change_for_max_area(m))
    print(name_islands(m))
