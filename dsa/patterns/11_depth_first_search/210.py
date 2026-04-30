from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        outp = []
        hmap = defaultdict(list)
        vstd = set()
        stak = set()
        def recur(node):
            if node in stak:
                return True
            if node in vstd:
                return False
            stak.add(node)
            for it in hmap.get(node, []):
                if recur(it):
                    return True
            stak.remove(node)
            if node not in vstd:
                vstd.add(node)
                outp.append(node)
        for a, b in prerequisites:
            hmap[a].append(b)
        for i in range(numCourses):
            if recur(i):
                return []
        return outp

if __name__ == '__main__':
    o = Solution()
    print(o.findOrder(2, [[1,0]]))
    print(o.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(o.findOrder(1, []))
    print(o.findOrder(2, [[0,1],[1,0]]))
    print(o.findOrder(11, [[1,0],[2,0],[2,1],[3,1],[3,2],[4,2],[4,3],[5,3],[5,4],[6,4],[6,5],[7,5],[7,6],[8,6],[8,7],[9,7],[9,8],[10,8],[10,9]]))
