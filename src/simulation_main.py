import numpy
from EnviromentalVariables import EnviromentalVariables
from EnvironmentalConstants import EnviromentalConstants
from SimulationEngine import SimulationEngine
from UsersList import UsersList
from src.EventList import EventList
from src.MyRandomGenerator import RandomNumberGenerator
from src.event.CreateUser import CreateUser

activeUsersList = UsersList
eventList = EventList
enviromentalVariables = EnviromentalVariables(0)

globalTime = 0


while():
    SimulationEngine.createUser()


for i in range(1,10):
    print(RandomNumberGenerator.get_random_number())


def createUser():
    eventList.append(CreateUser())