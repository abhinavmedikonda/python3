from collections import deque
from tree import Btree

def bfs(btree):
    q = deque([None, btree])
    level = 0
    while len(q) > 1:
        first = q.popleft()
        if first == None:
            print(f'level: {level}')
            q.append(None)
            level += 1
            continue
        print(first.data)
        if(first.left):
            q.append(first.left)
        if(first.right):
            q.append(first.right)

if __name__ == '__main__':
    btree = Btree.build([0, 1, 2, None, 4, 5, None, 7, None, 9])
    bfs(btree)

    btree = Btree.build(range(50))
    Btree.print(btree)