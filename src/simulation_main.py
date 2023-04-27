from src.environment.EnvironmentVariables import EnvironmentVariables
from src.SimulationEngine import SimulationEngine
from src.event.Event import Event


#
class main:
    environmentVariables = EnvironmentVariables.getInstance()
    Event.eventList = environmentVariables.eventList
    print(environmentVariables.inServiceUserList.userCount)


    SimulationEngine.createAddUserEvent()


    while not environmentVariables.eventList.isEnd():
        event: Event = environmentVariables.eventList.getNext()
        environmentVariables.globalTime = event.timeOfTheEvent
        event.serve()

        #print(str(event))
