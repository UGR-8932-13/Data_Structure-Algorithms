class WeightedGraph:
    def __init__(self, edges, n):
        self.edges = edges
        self.n = n

    def printWeightedEdges(self):
        print("The number of vertices is:", self.n)
        for i in range(self.n):
            vertex_str = "Vertex " + str(i) + ":"
            edges_str = ""
            for edge in self.edges:
                if edge.u == i:
                    edges_str += " (" + str(edge.u) + ", " + str(edge.v) + ", " + str(edge.w) + ")"
                elif edge.v == i:
                    edges_str += " (" + str(edge.v) + ", " + str(edge.u) + ", " + str(edge.w) + ")"
            print(vertex_str + edges_str)
            
    def getWeight(self, edge):
        return edge.w

    def getMinimumSpanningTree(self):
        disjoint_set = DisjointSet(self.n)
        result = []
        self.edges.sort(key=self.getWeight)
        for edge in self.edges:
            if disjoint_set.find(edge.u) != disjoint_set.find(edge.v):
                result.append(edge)
                disjoint_set.union(edge.u, edge.v)
        return WeightedGraph(result, self.n)

    def getTotalWeight(self):
        w = 0
        for edge in self.edges:
            w += edge.w
        return w

    def getRoot(self):
        root = -1
        for i in range(self.n):
            if all(edge.v != i for edge in self.edges):
                root = i
                break
        return root

    def getEdges(self):
        edges = []
        for edge in self.edges:
            edges.append((edge.u, edge.v))
        return edges


class DisjointSet:
    def __init__(self, num_elements):
        self.parent = list(range(num_elements))
        self.size = [0] * num_elements

    def make_set(self, element):
        self.parent[element] = element
        self.size[element] = 0

    def find(self, element):
        if element == self.parent[element]:
            return element
        self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, element_a, element_b):
        root_a = self.find(element_a)
        root_b = self.find(element_b)
        if root_a != root_b:
            if self.size[root_a] < self.size[root_b]:
                root_a, root_b = root_b, root_a
            self.parent[root_b] = root_a
            if self.size[root_a] == self.size[root_b]:
                self.size[root_a] += 1


class WeightedEdge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


filename = input("Enter the name of the file: ")

with open(filename, "r") as file:
    n = int(file.readline())
    edges = []
    for line in file:
        triplets = line.strip().split("|")
        for triplet in triplets:
            u, v, w = map(int, triplet.split(","))
            edges.append(WeightedEdge(u, v, w))

graph = WeightedGraph(edges, n)
graph.printWeightedEdges()

tree = graph.getMinimumSpanningTree()
print("Total weight is:", tree.getTotalWeight())
print("Root is:", tree.getRoot())
print("Edges are: ", end ="")
for edge in tree.getEdges():
    print("(" + str(edge[0]) + ", " + str(edge[1]) + ")", end =" ")
