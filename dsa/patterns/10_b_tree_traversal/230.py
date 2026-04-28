from ...trees.tree import Btree

# python -m dsa.patterns.10_b_tree_traversal.230

class Solution:
    def kthSmallest(self, root: Btree | None, k: int) -> int:
        def recur(node, k, i):
            if not node:
                return None, i
            v, i = recur(node.left, k, i)
            if v != None:
                return v, None
            if i+1 == k:
                return node.data, None
            v, i = recur(node.right, k, i+1)
            if v != None:
                return v, None
            return None, i

        return recur(root, k, 0)[0]

if __name__ == '__main__':
    o = Solution()
    print(o.kthSmallest(Btree.build([3,1,4,None,2]), 1))
    print(o.kthSmallest(Btree.build([5,3,6,2,4,None,None,1]), 3))
