import numpy as np
class RandomSet:
    def __init__(self, _values ,size):
        self._rng = np.random.default_rng()
        self._values = self._rng.integers(1, 1001, size=size)
        self._index = 0

    def getNextRandom(self):
        if self._index >= len(self._values):
            self._values = np.concatenate([self._values, self._rng.integers(1, 1001, size=100000)])
        value = self._values[self._index]
        self._index += 1
        return value