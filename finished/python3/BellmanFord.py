
# note this algorithm is used when there is negative edges present in the graph

# graph: a list of lists of tuples [ [ (edgeCost, w), ...], ...]
# start: starting vertex as index into graph
# Output: the shortest distance to all vertices from start vertex
def BellmanFord(graph, start):
    distance = [float("inf")]*len(graph)
    distance[start] = 0
    # repeat |V|-1 times
    for _ in range(len(graph)-1):
        # for all edges in E
        for u in range(len(graph)):
            for edgeCost, v in graph[u]:
                # update(e)
                distance[v] = min(distance[v], distance[u] + edgeCost)
    return distance