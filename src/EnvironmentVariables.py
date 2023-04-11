from src.EventList import EventList
from src.InQueForServiceUserList import InQueForServiceUserList
from src.InServiceUserList import InServiceUserList


class EnvironmentVariables:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.usersCounter = 0
            cls.__instance.eventList = EventList()
            cls.__instance.inServiceUserList = InServiceUserList()
            cls.__instance.inQueForServiceUserList = InQueForServiceUserList()
            cls.__instance.globalTime = 0
        return cls.__instance

    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        if EnvironmentVariables.__instance is None:
            EnvironmentVariables()
        return EnvironmentVariables.__instance
