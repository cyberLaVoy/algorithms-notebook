from queue import PriorityQueue

# note this algorithm does not work in the presence of negative edges

# graph: a list of lists of tuples [ [ (edgeCost, w), ...], ...]
# start: starting vertex as index into graph
# Output: the shortest distance to all vertices from start vertex
def Dijkstra(graph, start):
    distance = [None]*len(graph)
    queue = PriorityQueue()
    queue.put( (0, start) ) # tuple must be in this order for sorting purposes
    while not queue.empty():
        pathCost, u = queue.get()
        if distance[u] is None:
            distance[u] = pathCost
            for edgeCost, v in graph[u]:
                if distance[v] is None:
                    queue.put( (pathCost + edgeCost, v) )
    return distance