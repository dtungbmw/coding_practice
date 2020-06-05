from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(5, 6)

# Breadth First Search or BFS for a Graph
# Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree (See method 2
# of this post). The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same
# node again. To avoid processing a node more than once, we use a boolean visited array. For simplicity,
# it is assumed that all vertices are reachable from the starting vertex.

queue = []
def bfs(n):
    queue.append(n)
    while len(queue) != 0:
        n=queue.pop(0)
        print(n)
        children = g.graph[n]
        for c in children:
            queue.append(c)

bfs(0)

print("-"*100)
# Deapth First Search or BFS for a Graph
stack = []
def dfs(n):

    stack.append(n)
    while len(stack) != 0:
        n=stack.pop()
        print(n)
        children = g.graph[n]
        for c in children:
            stack.append(c)

dfs(0)