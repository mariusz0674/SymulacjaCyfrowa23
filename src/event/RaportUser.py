from src.EnvironmentVariables import EnvironmentVariables
from src.EnvironmentalConstants import EnvironmentalConstants
from src.event.Event import Event


class RaportUser(Event):
    def __init__(self, timeOfTheEvent, user = None):
        super().__init__(timeOfTheEvent, user)
        self.eventList.append(self)

    def serve(self):
        self.user.raport()
        if self.user.checkIsEndRoute():
            self.user.goDie()
        else:
            RaportUser(
                self.environmentVariables.globalTime + EnvironmentalConstants.USER_RAPORT_PERIOD,
                self.user
            )


    def __str__(self) -> str:
        return self.__class__.__name__ \
            + " at time: " \
            + str(self.timeOfTheEvent)
