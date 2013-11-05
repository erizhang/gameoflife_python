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
        g = Game(3, "1101101o00")
        count = g.aliveNeighbourCount(0, 0)
        self.assertEqual(3, count, "Can not calculate exact count of corrner");


class TestNextGeneration(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def testAllWillDieGeneration(self):
        g = Game(3, "100010000")
        next_gen = g.nextGeneration()
        self.assertEqual("000000000", next_gen, "Simple Generation is failure")


if __name__ == "__main__":
    unittest.main()
