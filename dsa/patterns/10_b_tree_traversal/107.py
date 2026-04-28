from collections import deque
from ...trees.tree import Btree

# python -m dsa.patterns.10_b_tree_traversal.107

class Solution:
    def levelOrderBottom(self, root: Btree | None) -> list[list[int]]:
        if not root:
            return []
        deq = deque()
        outp = []
        arr = []
        deq.extend([root, None])
        while deq:
            it = deq.popleft()
            if not it:
                outp.append(arr)
                arr = []
                if not deq:
                    break
                deq.append(None)
                continue
            arr.append(it.data)
            if it.left:
                deq.append(it.left)
            if it.right:
                deq.append(it.right)
        outp.reverse()
        return outp

if __name__ == '__main__':
    o = Solution()
    print(o.levelOrderBottom(Btree.build([3,9,20,None,None,15,7])))
    print(o.levelOrderBottom(Btree.build([1])))
    print(o.levelOrderBottom(Btree.build([])))
