class Graph:
    def __init__(self, data = 0, neighbors = None):
        self.data = data
        self.neighbors: list["Graph"] = []
    def from_lists(arays):
        hash = {}
        for i, aray in enumerate(arays, 1):
            node = hash.get(i, Graph(i))
            hash[i] = node
            for it in aray:
                n = hash.get(it, Graph(it))
                hash[it] = n
                node.neighbors.append(n)
        return hash[1] if hash else None
    def print_lists(graph):
        def recur(graph, vstd, hash):
            if not graph or graph in vstd:
                return
            vstd.append(graph)
            hash[graph.data] = []
            for it in graph.neighbors:
                if it.data not in hash[graph.data]:
                    hash[graph.data].append(it.data) 
                recur(it, vstd, hash)
        hash = {}
        vstd = []
        recur(graph, vstd, hash)
        print([hash[it] for it in sorted(hash)])
