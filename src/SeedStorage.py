class SeedStorage:
    _instance = None
    _seed = 2137

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def getSeed(cls):
        return cls._seed

    @classmethod
    def setSeed(cls, seed):
        cls._seed = seed