import sys
from ...trees.tree import Btree

# python -m dsa.patterns.10_b_tree_traversal.124

class Solution:
    def maxPathSum(self, root: Btree | None) -> int:
        def recur(node):
            if not node:
                return -sys.maxsize, -sys.maxsize
            lm, lc = recur(node.left)
            rm, rc = recur(node.right)
            nc = max(lc+node.data, rc+node.data, node.data)
            return max(nc, lm, rm, lc+rc+node.data), nc

        return recur(root)[0]

if __name__ == '__main__':
    o = Solution()
    print(o.maxPathSum(Btree.build([1,2,3])))
    print(o.maxPathSum(Btree.build([-10,9,20,None,None,15,7])))
    print(o.maxPathSum(Btree.build([5,4,8,11,None,13,4,7,2,None,None,None,1])))
