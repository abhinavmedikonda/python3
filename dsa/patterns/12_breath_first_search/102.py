from collections import deque
from ...trees.tree import Btree

# python -m dsa.patterns.12_breath_first_search.102

class Solution:
    def levelOrder(self, root: Btree | None) -> list[list[int]]:
        if not root:
            return []
        outp = []
        deq = deque([root, None])
        aray = []
        while True:
            node = deq.popleft()
            if not node:
                outp.append(aray)
                aray = []
                if not deq:
                    break
                deq.append(None)
                continue
            aray.append(node.data)
            if node.left:
                deq.append(node.left)
            if node.right:
                deq.append(node.right)
        return outp

if __name__ == '__main__':
    o = Solution()
    print(o.levelOrder(Btree.build([3,9,20,None,None,15,7])))
    print(o.levelOrder(Btree.build([1])))
    print(o.levelOrder(Btree.build([])))
