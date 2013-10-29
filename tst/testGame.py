import sys
sys.path.append('../')
from gamePackage import Game
import unittest

class TestAliveNeighbourCount(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def testOnlyOneAliveNeighbour(self):
        g = Game(3, "100010000")
        count = g.aliveNeighbourCount(1, 1)
        self.assertEqual(1, count, "alive neighbour count is wrong");

    def testFullAliveNeighbour(self):
        g = Game(3, "111111111")
        count = g.aliveNeighbourCount(1, 1)
        self.assertEqual(8, count, "full alive neighbour count is wrong");

    def testCountAliveNeighborOfCorrner(self):
        g = Game(3, "110110100")
        count = g.aliveNeighbourCount(0, 0)
        self.assertEqual(3, count, "Can not calculate exact count of corrner");

if __name__ == "__main__":
    unittest.main()
