class Event:

    def __init__(self, timeOfTheEvent):
        self.timeOfTheEvent = timeOfTheEvent


    def doNothing(self):
        return "null"

    def serve(self):
        raise NotImplementedError()

