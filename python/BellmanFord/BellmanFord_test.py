import unittest
from BellmanFord import BellmanFord

class TestBellmanFord(unittest.TestCase):
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

        # compute the distances using the BellmanFord algorithm
        distances = BellmanFord(graph, 0)

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

        # compute the distances using the BellmanFord algorithm
        distances = BellmanFord(graph, 0)

        # compare the computed distances with the expected values
        self.assertEqual(distances, expected)

    def test_with_a_negative_weight(self):
        # define a graph with a negative weight for testing
        graph = [
            [ (-1, 1), (1, 2) ], # edges from vertex 0
            [ (1, 2), (4, 1) ],  # edges from vertex 1
            [ (0, 0), (6, 3) ],  # edges from vertex 2
            [ (3, 0) ]           # edges from vertex 3
        ]

        # expected distances from start vertex 0
        expected = [0, -1, 0, 6]

        # compute the distances using the BellmanFord algorithm
        distances = BellmanFord(graph, 0)

        # compare the computed distances with the expected values
        self.assertEqual(distances, expected)

    def test_with_disconnected_node(self):
        # define a graph with a disconnected node for testing
        graph = [
            [ (0, 1), (1, 2) ],  # edges from vertex 0
            [ (1, 2), (0, 1) ],  # edges from vertex 1
            [ (0, 0) ],          # edges from vertex 2
            [ (0, 0) ]           # edges from vertex 3
        ]

        # expected distances from start vertex 0
        expected = [0, 0, 1, float("inf")]

        # compute the distances using the BellmanFord algorithm
        distances = BellmanFord(graph, 0)

        # compare the computed distances with the expected values
        self.assertEqual(distances, expected)



if __name__ == '__main__':
    unittest.main()