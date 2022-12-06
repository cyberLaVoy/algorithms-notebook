import unittest
from Dijkstra import Dijkstra

class TestDijkstra(unittest.TestCase):
    def test_simple_case(self):
        # define a simple graph for testing
        graph = [
            [ (1, 2), (3, 4) ],  # edges from vertex 0
            [ (2, 3) ],          # edges from vertex 1
            [ (1, 4) ],          # edges from vertex 2
            [ (2, 0) ],          # edges from vertex 3
            [ (2, 1) ]           # edges from vertex 4
        ]

        # expected distances from start vertex 0
        expected = [0, 4, 1, 6, 2]

        # compute the distances using the Dijkstra algorithm
        distances = Dijkstra(graph, 0)

        # compare the computed distances with the expected values
        self.assertEqual(distances, expected)

    def test_complex_case(self):
        # define a more complex graph for testing
        graph = [
            [ (1, 2), (3, 4), (2, 3) ],  # edges from vertex 0
            [ (5, 4) ],                  # edges from vertex 1
            [ (1, 4), (2, 1) ],          # edges from vertex 2
            [ (2, 0), (4, 1) ],          # edges from vertex 3
            [ (2, 1), (3, 0) ]           # edges from vertex 4
        ]

        # expected distances from start vertex 0
        expected = [0, 3, 1, 2, 2]

        # compute the distances using the Dijkstra algorithm
        distances = Dijkstra(graph, 0)

        # compare the computed distances with the expected values
        self.assertEqual(distances, expected)


if __name__ == '__main__':
    unittest.main()