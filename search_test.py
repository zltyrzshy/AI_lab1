import unittest

import search
from problems import FifteensNode

boards = [[[5, 6, 4, 12], [11, 14, 9, 1], [0, 3, 8, 15], [10, 7, 2, 13]],
          [[1, 15, 7, 10], [9, 14, 4, 11], [8, 5, 0, 6], [13, 3, 2, 12]],
          [[1, 7, 8, 10], [6, 9, 15, 14], [13, 3, 0, 4], [11, 5, 12, 2]],
          [[14, 2, 8, 1], [7, 10, 4, 0], [6, 15, 11, 5], [9, 3, 13, 12]],
          [[1, 3, 2, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]],
          [[1, 3, 2, 4], [8, 6, 7, 5], [9, 10, 11, 12], [13, 14, 15, 0]],
          [[1, 3, 2, 12], [8, 6, 7, 5], [9, 10, 11, 4], [13, 14, 15, 0]],
          [[10, 3, 2, 12], [8, 6, 7, 5], [9, 1, 11, 4], [13, 14, 15, 0]],
          [[10, 3, 0, 12], [8, 6, 7, 5], [9, 1, 11, 4], [13, 14, 15, 2]],
          [[10, 3, 5, 12], [8, 6, 7, 0], [9, 1, 11, 4], [13, 14, 15, 2]],
          [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 11], [13, 14, 15, 12]]]
final_str = "1  2  3  4\n5  6  7  8\n9 10 11 12\n13 14 15  0"

class SearchTest(unittest.TestCase):
    def test_Astar(self):
        path_final = search.Astar(FifteensNode(input_str=final_str))

        self.assertTrue(path_final)

        for board in boards:
            node = FifteensNode(board=board)
            path = search.Astar(node)

            self.assertTrue(path)

            print('success')