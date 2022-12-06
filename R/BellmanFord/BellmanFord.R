# note this algorithm is used when there is negative edges present in the graph

# graph: a list of lists of tuples list( list( c(edgeCost, w), ...), ...)
# start: starting vertex as index into graph
# Output: the shortest distance to all vertices from start vertex
BellmanFord <- function(graph, start) {
  distance <- rep(Inf, length(graph))
  distance[start] <- 0
  # repeat |V|-1 times
  for (i in 1:(length(graph)-1)) {
    # for all edges in E
    for (u in 1:length(graph)) {
      for (edge in  graph[[u]]) {
        edgeCost <- edge[1]
        v <- edge[2]
        # update(e)
        distance[v] <- min(distance[v], distance[u] + edgeCost)
      }
    }
  }
  return(distance)
}