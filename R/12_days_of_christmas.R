presentsOnGivenDay <- function(day) {
  return(day * (day + 1) / 2) # triangular number
}

presentsTotal <- function(day) {
  return(day * (day + 1) * (day + 2) / 6) # tetrahedral number
}
