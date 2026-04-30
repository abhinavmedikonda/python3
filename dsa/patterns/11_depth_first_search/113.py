from ...trees.tree import Btree
import copy

# python -m dsa.patterns.11_depth_first_search.113

class Solution:
    def pathSum(self, root: Btree, targetSum: int) -> list[list[int]]:
        def recur(node, trgt, outp, stak, summ):
            if not node:
                return summ
            stak.append(node.data)
            summ += node.data
            summ = recur(node.left, trgt, outp, stak, summ)
            summ = recur(node.right, trgt, outp, stak, summ)
            if summ == trgt and not node.left and not node.right:
                outp.append(copy.deepcopy(stak))
            summ -= stak.pop()
            return summ

        outp = []
        stak = []
        recur(root, targetSum, outp, stak, 0)
        return outp

if __name__ == '__main__':
    o = Solution()
    print(o.pathSum(Btree.build([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]), 22))
    print(o.pathSum(Btree.build([1,2,3]), 5))
    print(o.pathSum(Btree.build([1,2]), 0))
