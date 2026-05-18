from collections import deque
from tree import Btree

def is_bst(btree):
    def recur(btree):
        if not btree:
            return(float('inf'), float('-inf'))
        l = recur(btree.left)
        if not l or l[1] >= btree.data:
            return False
        r = recur(btree.right)
        if not r or r[0] <= btree.data:
            return False
        return (min(l[0], btree.data), max(r[1], btree.data))
    return True if recur(btree) else False
def isbst(btree, mn=float('-inf'), mx=float('inf')):
    if not btree:
        return True
    if btree.data <= mn or btree.data >= mx:
        return False
    return isbst(btree.left, mn, btree.data) and isbst(btree.right, btree.data, mx)

if __name__ == '__main__':
    btree = Btree.build([0, 1, 2, None, 4, 5, 6, None, None, 9])
    Btree.print(btree)
    print(is_bst(btree))
    print()
    btree = Btree.build([5, 2, 6, 1, 4, None, 7, 0, None, 3])
    Btree.print(btree)
    print(is_bst(btree))
    print()
    print()
    btree = Btree.build([0, 1, 2, None, 4, 5, 6, None, None, 9])
    Btree.print(btree)
    print(isbst(btree))
    print()
    btree = Btree.build([5, 2, 6, 1, 4, None, 7, 0, None, 3])
    Btree.print(btree)
    print(isbst(btree))
