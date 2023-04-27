from src.environment.EnvironmentalConstants import EnvironmentalConstants
from src.event.Event import Event


class RaportUser(Event):
    def __init__(self, timeOfTheEvent, user = None):
        super().__init__(timeOfTheEvent, user)
        self.eventList.append(self)


    def killUser(self):
        self.environmentVariables.usersCounter=-1
        self.environmentVariables.inServiceUserList.remove(self.user)
    def pushUserToServe(self):
        self.environmentVariables.inServiceUserList.append(self.user)
        RaportUser(
            self.environmentVariables.globalTime + EnvironmentalConstants.USER_RAPORT_PERIOD,
            self.user
        )
        print("User from que")

    def serve(self):
        self.user.raport()
        if self.user.checkIsEndRoute():
            self.killUser()
            self.pushUserToServe()

            print("die")
        else:
            RaportUser(
                self.environmentVariables.globalTime + EnvironmentalConstants.USER_RAPORT_PERIOD,
                self.user
            )


    def __str__(self) -> str:
        return self.__class__.__name__ \
            + " at time: " \
            + str(self.timeOfTheEvent)
