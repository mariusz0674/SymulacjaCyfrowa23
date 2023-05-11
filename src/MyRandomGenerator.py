import random
import numpy as np
from src.RandomUniform import RandomUniform

# class RandomNumberGenerator:
#     _rng = random.Random()
#
#     @staticmethod
#     def getRandomSpeed():
#         return RandomNumberGenerator._rng.randint(50, 500)
#
#     @staticmethod
#     def get_random_number():
#         return RandomNumberGenerator._rng.randint(1, 1000)
#
#     @staticmethod
#     def getRandomUserCreateTime():
#         return RandomNumberGenerator._rng.randint(1, 600)
#
#
#     @staticmethod
#     def getRandomNormal() -> float:
#         #return random.Random().gauss(0, 4)
#         return RandomNumberGenerator._rng.gauss(0, 4)
#
#

class RandomNumberGenerator:
    _rng = np.random.default_rng()
    #uniformRandom = RandomUniform(1, 1001, 100000)
    userCreateTimeGenerator = RandomUniform(1, 601, 100000)
    @staticmethod
    def getRandomSpeed():
        return RandomNumberGenerator._rng.integers(50, 501)

    # @staticmethod
    # def get_random_number():
    #     #return RandomNumberGenerator._rng.integers(1, 1001)
    #     return RandomNumberGenerator.uniformRandom.getNextRandom()

    @staticmethod
    def getRandomUserCreateTime():
        #return RandomNumberGenerator._rng.integers(1, 601)
        return RandomNumberGenerator.userCreateTimeGenerator.getNextRandom()
    @staticmethod
    def getRandomNormal() -> float:
        return RandomNumberGenerator._rng.normal(0, 4)

