from ...trees.tree import Btree

# python -m dsa.patterns.10_b_tree_traversal.257

class Solution:
    def binaryTreePaths(self, root: Btree | None) -> list[str]:
        def recur(node, path, outp):
            if not node:
                return
            path += str(node.data)
            if not node.left and not node.right:
                return outp.append(path)
            recur(node.left, f'{path}->', outp)
            recur(node.right, f'{path}->', outp)

        outp = []
        recur(root, '', outp)
        return outp

if __name__ == '__main__':
    o = Solution()
    print(o.binaryTreePaths(Btree.build([1,2,3,None,5])))
    print(o.binaryTreePaths(Btree.build([1])))
