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

    def testNextGenerationAlongToDie(self):
        g = Game(3, "000010000")
        next_gen = g.nextGeneration()
        self.assertEqual("000000000", next_gen, "Along to die is failure")

    def testNextGenerationCrowdedToDie(self):
        g = Game(3, "111111111")
        next_gen = g.nextGeneration()
        self.assertEqual("101000101", next_gen, "Crowded to die is failure")

    def testNextGenerationStableAlive(self):
        g = Game(3, "110110000")
        next_gen = g.nextGeneration()
        self.assertEqual("110110000", next_gen, "Stable alive is failure")

    def testNextGenerationRecover(self):
        g = Game(3, "010101000")
        next_gen = g.nextGeneration()
        self.assertEqual("010010000", next_gen, "Recover is failure")


if __name__ == "__main__":
    unittest.main()
