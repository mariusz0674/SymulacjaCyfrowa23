import numpy as np
from src.RandomSet import RandomSet
from src.SeedStorage import SeedStorage
class RandomUniform():
    def __init__(self, lLimit, uLimit, size):
        self.seedStorage = SeedStorage()
        self.lLimit = lLimit
        self.uLimit = uLimit
        self.size = size
        self._rng = np.random.default_rng(self.seedStorage.getSeed())
        self._values = self._rng.integers(self.lLimit, self.uLimit, size=size)
        self.seedStorage.setSeed(self._values[-1])
        self._index=0
        #super().__init__(self._values, size)


    def getNextRandom(self):
        if self._index >= len(self._values):
            self._values = self._rng.integers(self.lLimit, self.uLimit, self.size)
            self.seedStorage.setSeed(self._values[-1])
            self._index = 0
        value = self._values[self._index]
        self._index += 1
        return value