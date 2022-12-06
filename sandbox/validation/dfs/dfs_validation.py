from dfs import edgeTypes, dfs, stronglyConnectedComponents, metaGraphEdges

def edgeTypeTest():
    graph = []
    for i in range(8):
        graph.append([])
    graph[0].extend([1,2,5]) 
    graph[1].extend([4]) 
    graph[2].extend([3]) 
    graph[3].extend([0, 7]) 
    graph[4].extend([5, 6, 7]) 
    graph[5].extend([1, 6]) 
    graph[6].extend([]) 
    graph[7].extend([6])
    _, pre, post = dfs(graph)
    treeOrForward, back, cross = edgeTypes(graph, pre, post)
    print(treeOrForward)
    print(back)
    print(cross)

def stronglyConnectedComponentsTest():
    graph = []
    for i in range(12):
        graph.append([])
    graph[0].extend([1]) 
    graph[1].extend([2,3,4]) 
    graph[2].extend([5]) 
    graph[3].extend([]) 
    graph[4].extend([1,5,6]) 
    graph[5].extend([2,7]) 
    graph[6].extend([7,9]) 
    graph[7].extend([10])
    graph[8].extend([6])
    graph[9].extend([8])
    graph[10].extend([11])
    graph[11].extend([9])
    scc, actualEdges, metaEdges = stronglyConnectedComponents(graph)
    print(scc)
    print(actualEdges)
    print(metaEdges)


def main():
    #edgeTypeTest()
    stronglyConnectedComponentsTest()


if __name__ == "__main__":
    main()