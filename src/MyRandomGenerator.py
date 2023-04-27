import random


class RandomNumberGenerator:
    _rng = random.Random()

    @staticmethod
    def get_random_number():
        return RandomNumberGenerator._rng.randint(1, 1000)

    @staticmethod
    def getRandomUserCreateTime():
        return RandomNumberGenerator._rng.randint(1, 1000)


    @staticmethod
    def getRandomNormal() -> float:
        return random.Random().gauss(0, 4)

