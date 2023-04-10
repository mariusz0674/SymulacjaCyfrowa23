from src.event.Event import Event

class CreateUser(Event):
    def __init__(self, timeOfTheEvent):
        super().__init__(timeOfTheEvent)

    def serve(self):

        pass
