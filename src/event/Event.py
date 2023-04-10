from src.EnvironmentVariables import EnvironmentVariables


class Event:
    eventList = None
    environmentVariables = EnvironmentVariables.getInstance()

    def __init__(self,
                 timeOfTheEvent,
                 user=None):
        self.timeOfTheEvent = timeOfTheEvent
        self.user = user


    def doNothing(self):
        return "null"

    def serve(self):
        raise NotImplementedError()


    def __str__(self) -> str:
        raise NotImplementedError()
