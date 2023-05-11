import random


class RandomNumberGenerator:
    _rng = random.Random()


    @staticmethod
    def getRandomSpeed():
        return RandomNumberGenerator._rng.randint(50, 500)

    @staticmethod
    def get_random_number():
        return RandomNumberGenerator._rng.randint(1, 1000)

    @staticmethod
    def getRandomUserCreateTime():
        return RandomNumberGenerator._rng.randint(1, 600)


    @staticmethod
    def getRandomNormal() -> float:
        #return random.Random().gauss(0, 4)
        return RandomNumberGenerator._rng.gauss(0, 4)


