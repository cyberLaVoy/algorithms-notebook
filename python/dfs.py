
def explore(graph, v, visited, ccnum, cc, pre, post, clock):
    visited[v] = True
    # previsit
    ccnum[v] = cc
    pre[v] = clock[0]
    clock[0] += 1
    for u in graph[v]:
        if not visited[u]:
            explore(graph, u, visited, ccnum, cc, pre, post, clock)
    # postvisit
    post[v] = clock[0]
    clock[0] += 1

# graph: a list of lists (adjacency list) [ [ w0, w1, ...], ...]
# order: an optional list determining the order of vertex processing
# Output: the conected component, previsit, and postvisit numbers for each vertex
def dfs(graph, order=None):
    visited = [False]*len(graph)
    ccnum = [-1]*len(graph)
    pre = [-1]*len(graph)
    post = [-1]*len(graph)
    cc = -1
    clock = [1]
    if order is None:
        order = range(len(graph))
    for v in order:
        if not visited[v]:
            cc += 1
            explore(graph, v, visited, ccnum, cc, pre, post, clock)
    return ccnum, pre, post


# AUXILLARY FUNCTIONS for directed graphs

# returns all edge types in directed graph
# note if the list back edges is not empty, there is a cycle in the graph
def edgeTypes(graph, pre, post):
    treeOrForward = []
    back = []
    cross = []
    for u in range(len(graph)):
        for v in graph[u]: 
            if pre[u] < pre[v] and pre[v] < post[v] and post[v] < post[u]:
                treeOrForward.append((u, v))
            elif pre[v] < pre[u] and pre[u] < post[u] and post[u] < post[v]:
                back.append((u, v))
            elif pre[v] < post[v] and post[v] < pre[u] and pre[u] < post[u]:
                cross.append((u,v))
    return treeOrForward, back, cross       

# returns an adjacency list as a reversed version of the original directed graph
def reversedGraph(graph):
    graphReversed = []
    for i in range(len(graph)):
        graphReversed.append([])
    for u in range(len(graph)):
        for v in graph[u]: 
            graphReversed[v].append(u)
    return graphReversed

# returns the order of vertices from decreasing postvisit values
def decreasingPostNumberOrder(post):
    hashMap = [None]*(max(post)+1)
    for i in range(len(post)):
        hashMap[post[i]] = i
    order = []
    for value in hashMap:
        if value is not None:
            order.append(value)
    return reversed(order)

# returns the actual and meta edges that connect nodes in a directed meta-graph
# note graph must have been processed from decreasing postvisit values
def metaGraphEdges(ccnum, treeOrForward, cross):
    actualEdges = []
    metaEdges = []
    for edge in treeOrForward:
        if ccnum[edge[0]] != ccnum[edge[1]]:
            actualEdges.append(edge)
            metaEdges.append( (ccnum[edge[0]], ccnum[edge[1]]) )
    for edge in cross:
        if ccnum[edge[0]] != ccnum[edge[1]]:
            actualEdges.append(edge)
            metaEdges.append( (ccnum[edge[0]], ccnum[edge[1]]) )
    return actualEdges, metaEdges

# Output: a list of lists, each containing vertices in the respective strongly connected component;
# and the actual/meta edges that connect the meta-graph
def stronglyConnectedComponents(graph):
    _, _, post = dfs(reversedGraph(graph))
    ccnum, pre, post = dfs(graph, decreasingPostNumberOrder(post))
    stronglyConnectedComponents = []
    for i in range(max(ccnum)+1):
        stronglyConnectedComponents.append([])
    for i in range(len(ccnum)):
        stronglyConnectedComponents[ccnum[i]].append(i)
    treeOrForward, _, cross = edgeTypes(graph, pre, post)
    actualEdges, metaEdges = metaGraphEdges(ccnum, treeOrForward, cross)
    return stronglyConnectedComponents, actualEdges, metaEdges