from src.environment.EnvironmentalConstants import EnvironmentalConstants
from src.event.Event import Event
from src.BaseStationId import BaseStationId

class RaportUser(Event):
    def __init__(self, timeOfTheEvent, user = None):
        super().__init__(timeOfTheEvent, user)
        self.eventList.append(self)

    def killUser(self):
        self.environmentVariables.statisticEngine.appendUserStatisticPack(self.user.userStatistic)
        self.environmentVariables.usersservedCounter += 1
        # if self.user.userStatistic.baseSwitches > 1 :
        #     print("User " + str(self.user.userStatistic.userID) + " switched base station " + str(self.user.userStatistic.baseSwitches) + " times")
        #     pass
        self.environmentVariables.inServiceUserList.remove(self.user)

        if self.user.basestationID == "BS1":
                self.user.userStatistic.endStation = BaseStationId.BS1
        else:
                self.user.userStatistic.endStation = BaseStationId.BS2

    def pushUserToServeIfWaiting(self):
        if self.environmentVariables.inQueForServiceUserList.isEmpty():
            return
        userToActive = self.environmentVariables.inQueForServiceUserList.pop()
        self.environmentVariables.inServiceUserList.append(userToActive)
        RaportUser(
            self.environmentVariables.globalTime + EnvironmentalConstants.USER_RAPORT_PERIOD,
            userToActive
        )
        #print("User from que")


    def serve(self):
        self.user.updatePosition()
        if self.user.checkIsEndRoute():
            self.killUser()
            self.pushUserToServeIfWaiting()
            #print("die")

            return
        else:
            RaportUser(
                self.environmentVariables.globalTime + EnvironmentalConstants.USER_RAPORT_PERIOD,
                self.user
            )
        self.user.raport()


    def __str__(self) -> str:
        return self.__class__.__name__ \
            + " at time: " \
            + str(self.timeOfTheEvent)
