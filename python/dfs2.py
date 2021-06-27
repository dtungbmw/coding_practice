
graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

graph2 = {
    'A' : ['B','D'],
    'B' : ['A', 'C'],
    'C' : ['B'],
    'D' : ['A'],

}

visited = []

stack = []


def dfs(node, graph):

    stack.append(node)

    while len(stack) >0:
        nextNode = stack.pop()
        if nextNode not in visited:
            visited.append(nextNode)
            kids = reversed(graph[nextNode])
            for kid in kids:
                stack.append(kid)


dfs('A',graph2)

print(visited)



