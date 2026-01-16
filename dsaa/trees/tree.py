import math


class Tree:
    def __init__(self, data):
        self.data = data
        self.children: list["Tree"] = []

class Btree:
    def __init__(self, data):
        self.data = data
        self.left: "Btree" = None
        self.right: "Btree" = None
    def build(arr):
        btree = Btree(arr[0])
        Btree.recur_build(arr, btree, 0)
        return btree
    def recur_build(arr, node, ind):
        lc = (ind*2)+1
        rc = lc+1
        if lc < len(arr) and arr[lc]:
            node.left = Btree(arr[lc])
            Btree.recur_build(arr, node.left, lc)
        if rc < len(arr) and arr[rc]:
            node.right = Btree(arr[rc])
            Btree.recur_build(arr, node.right, rc)
    # bst sequence
    def in_order(btree):
        if not btree:
            return
        Btree.in_order(btree.left)
        print(btree.data)
        Btree.in_order(btree.right)
    # dfs
    def pre_order(btree):
        if not btree:
            return
        print(btree.data)
        Btree.pre_order(btree.left)
        Btree.pre_order(btree.right)
    def post_order(btree):
        if not btree:
            return
        Btree.post_order(btree.left)
        Btree.post_order(btree.right)
        print(btree.data)
    def height(btree):
        if not btree:
            return 0
        return 1 + max(Btree.height(btree.left), Btree.height(btree.right))
    def level(index):
        return int(math.log(index+1, 2))
    def print(btree):
        outp = [str() for i in range(Btree.height(btree))]
        stack = []
        disp = 0
        curr = (btree, 0)
        while curr[0] or stack:
            while curr[0]:
                stack.append(curr)
                curr = (curr[0].left, (curr[1]*2)+1)
            curr = stack.pop(-1)
            empty = disp - len(outp[Btree.level(curr[1])])
            outp[Btree.level(curr[1])] += f'{" "*empty} {curr[0].data}'
            disp = len(outp[Btree.level(curr[1])])
            curr = (curr[0].right, (curr[1]*2)+2)
        [print(s) for s in outp]
