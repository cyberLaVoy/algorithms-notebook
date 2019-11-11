from BellmanFord import BellmanFord


def main():
    graph = [[] for _ in range(8)]
    graph[0].extend([(10,1), (8,7)])
    graph[1].extend([(2,5)])
    graph[2].extend([(1,2), (1,3)])
    graph[3].extend([(3,4)])
    graph[4].extend([(-1,5)])
    graph[5].extend([(-2,2)])
    graph[6].extend([(-1,5), (-4,1)])
    graph[7].extend([(1,6)])
    start = 0
    print(BellmanFord(graph, start))


if __name__ == "__main__":
    main()