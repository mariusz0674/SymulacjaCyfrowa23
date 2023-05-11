from src.BaseStationId import BaseStationId
class UserStatisticPack:

    def __init__(self, userID):
        self.userID = userID
        self.baseSwitches = 0
        self.endStation = BaseStationId.NONE
        self.wasConectionBroken = True
