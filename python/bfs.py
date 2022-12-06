from queue import Queue

# graph: a list of lists (adjacency list) [ [ w0, w1, ...], ...]
# start: starting vertex as index to adjacency list
# Output: the step-wise distance to all vertices from start vertex
def bfs(graph, start):
    distance = [None]*len(graph)
    distance[start] = 0
    queue = Queue() # FIFO queue
    queue.put(start)
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if distance[v] is None:
                queue.put(v)
                distance[v] = distance[u] + 1
    return distance
