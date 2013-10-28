import sys
sys.path.append('../')
from gamePackage import Game
import unittest

class TestAliveNeighbourCount(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def testOnlyOneNeighbour(self):
        g = Game("100010000")
        count = g.aliveNeighbourCount(1, 1)
        self.assertEqual(1, count, "alive neighbour count is wrong");

if __name__ == "__main__":
    unittest.main()
