import math

from src import MyRandomGenerator
from src.EnvironmentalConstants import EnvironmentalConstants
from src.EnvironmentVariables import EnvironmentVariables



class User:
    def __init__(self,
                 userID,
                 basestationID="BS1"):
        self.basestationID = basestationID
        self.userID = userID
        self.speed = MyRandomGenerator.RandomNumberGenerator.get_random_number() / 2
        self.position = EnvironmentalConstants.RESP_DIE
        self.positiveRaportsToSwitchCounter = 0

    def hangoverCheck(self):
        # implement your hangover check logic here
        pass

    def processSwitchContition(self, powBs1, powBs2):
        if self.basestationID == "BS1":
            if powBs2 >= powBs1:
                self.positiveRaportsToSwitchCounter+=1
            else:
                self.positiveRaportsToSwitchCounter=0
        else:
            if powBs2 <= powBs1:
                self.positiveRaportsToSwitchCounter+=1
            else:
                self.positiveRaportsToSwitchCounter=0


    def switchBase(self):
        self.positiveRaportsToSwitchCounter = 0
        if self.basestationID == "BS1":
            self.basestationID = "BS2"
        else:
            self.basestationID = "BS1"

        print("base changed to: " + self.basestationID)

    def raport(self):
        self.updatePosition()
        powBs1, powBs2 = self.calcReceivedPowers()
        self.processSwitchContition(powBs1, powBs2)
        if self.positiveRaportsToSwitchCounter >= 5:
            self.switchBase()





    def checkIsEndRoute(self):
        if self.position >= EnvironmentalConstants.DISTANCE_BEETWEN_STATIONS - EnvironmentalConstants.RESP_DIE:
            return True
        return False



    def updatePosition(self):
        self.position += self.speed * EnvironmentalConstants.USER_RAPORT_PERIOD / 1000

    def calcPower(self, distance):
        return 4.56 - 22 * math.log10(distance)

    def calcReceivedPowers(self):
        powBs1 = self.calcPower(self.position)
        powBs2 = self.calcPower(EnvironmentalConstants.DISTANCE_BEETWEN_STATIONS - self.position)
        return powBs1, powBs2

    def goDie(self):
        pass
    def __str__(self) -> str:
        return str(self.userID) + " : " + str(self.basestationID)
