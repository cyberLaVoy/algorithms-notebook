library(here)
source(here::here("R", "BellmanFord", "BellmanFord.R"))

# test the BellmanFord function
graph1 <- list(
  list(c(0, 2), c(1, 3)), # vertex 1
  list(c(1, 3), c(0, 2)), # vertex 2
  list(c(0, 1)),          # vertex 3
  list(c(0, 1))           # vertex 4
)

expected1 <- c(0, 0, 1, Inf)
result1 <- BellmanFord(graph1, 1)

if (identical(result1, expected1)) {
  print("BellmanFord test 1 passed.")
} else {
  print("BellmanFord test 1 failed.")
}

graph2 <- list(
  list(c(-1, 2), c(1, 3)), # vertex 1
  list(c(1, 3), c(4, 2)),  # vertex 2
  list(c(0, 1), c(6, 4)),  # vertex 3
  list(c(3, 1))            # vertex 4
)

expected2 <- c(0, -1, 0, 6)
result2 <- BellmanFord(graph2, 1)

if (identical(result2, expected2)) {
  print("BellmanFord test 2 passed.")
} else {
  print("BellmanFord test 2 failed.")
}
