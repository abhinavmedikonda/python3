from ...graphs.graph import Graph
# python -m dsa.patterns.11_depth_first_search.133

class Solution:
    def cloneGraph(self, node: Graph | None) -> Graph | None:
        def recur(node, hmap):
            if node in hmap:
                return hmap[node]
            n = Graph(node.data)
            hmap[node] = n
            for it in node.neighbors:
                n.neighbors.append(recur(it, hmap))
            return n
        hmap = {}
        return recur(node, hmap) if node else None

if __name__ == '__main__':
    o = Solution()
    Graph.print_lists(o.cloneGraph(Graph.from_lists([[2,4],[1,3],[2,4],[1,3]])))
    Graph.print_lists(o.cloneGraph(Graph.from_lists([[]])))
    Graph.print_lists(o.cloneGraph(Graph.from_lists([])))
