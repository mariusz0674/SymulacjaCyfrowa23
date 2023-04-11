from src.EnvironmentVariables import EnvironmentVariables
from src.EnvironmentalConstants import EnvironmentalConstants
from src.User import User
from src.event.Event import Event
from src.event.RaportUser import RaportUser


class AddUser(Event):
    def __init__(self, timeOfTheEvent):
        super().__init__(timeOfTheEvent)
        self.eventList.append(self)

    def serve(self):
        userCount = self.environmentVariables.usersCounter=+1
        self.user = User(userCount)
        if self.environmentVariables.inServiceUserList.userCount < EnvironmentalConstants.MAX_USSERS_IN_SYSTEM:
            self.environmentVariables.inServiceUserList.append(self.user)
            RaportUser(
                self.environmentVariables.globalTime + EnvironmentalConstants.USER_RAPORT_PERIOD,
                self.user
            )
        else:
            self.environmentVariables.inQueForServiceUserList.append(self.user)

    def __str__(self) -> str:
        return self.__class__.__name__ \
            + " at time: " \
            + str(self.timeOfTheEvent)
