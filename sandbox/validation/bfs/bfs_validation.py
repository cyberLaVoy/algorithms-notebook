from bfs import bfs


def main():
    graph = [[1,2],[2],[0,3],[3]] 
    assert bfs(graph, 2) == [1, 2, 0, 1] 
    graph = [[1,3],[0,2,3,4],[1,5],[0,1],[1,5],[2,4]]
    assert bfs(graph, 1) == [1, 0, 1, 1, 1, 2]

if __name__ == "__main__":
    main()
    print("All tests passed.")