from src import MyRandomGenerator
from src.environment.EnvironmentalConstants import EnvironmentalConstants
from src.User import User
from src.event.Event import Event
from src.event.RaportUser import RaportUser


class AddUser(Event):
    def __init__(self, timeOfTheEvent):
        super().__init__(timeOfTheEvent)
        self.eventList.append(self)

    def serve(self):
        self.environmentVariables.usersCounter += 1
        userCount = self.environmentVariables.usersCounter

        self.user = User(userCount)
        if self.environmentVariables.inServiceUserList.userCount < EnvironmentalConstants.MAX_USSERS_IN_SYSTEM:
            self.environmentVariables.inServiceUserList.append(self.user)
            RaportUser(
                self.environmentVariables.globalTime + EnvironmentalConstants.USER_RAPORT_PERIOD,
                self.user
            )
            self.environmentVariables.statisticEngine.addActiveUsersInTime(
                self.environmentVariables.globalTime,
                self.environmentVariables.inServiceUserList.userCount)
            #print("Add usser to in service")
        else:
            self.environmentVariables.inQueForServiceUserList.append(self.user)
            self.environmentVariables.statisticEngine.addInQueForServiceUsersInTime(
                self.environmentVariables.globalTime,
                self.environmentVariables.inQueForServiceUserList.userCount)

        AddUser(
            self.environmentVariables.globalTime + MyRandomGenerator.RandomNumberGenerator.getRandomUserCreateTime()
        )




    def __str__(self) -> str:
        return self.__class__.__name__ \
            + " at time: " \
            + str(self.timeOfTheEvent)
