import sys

class Game:
    def __init__(self, size, city):
        self.m_size = size
        self.m_city = city

    def __isAlive(self, col, row):
        if col < 0 or col >= self.m_size \
        or row < 0 or row >= self.m_size:
            return False

        pos = row * self.m_size + col
        if self.m_city[pos] == '1':
            return True
        return False

    def aliveNeighbourCount(self, col, row):
        offset = [[-1, -1], [-1, 0], [-1, 1], [0, -1], \
                  [0, 1], [1, -1], [1, 0], [1, 1]]
        count = 0
        for i in range(8):
            if self.__isAlive(col + offset[i][1], row + offset[i][0]) is True:
                count += 1
        return count
        
    
