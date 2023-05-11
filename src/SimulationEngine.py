from src import MyRandomGenerator
from src.environment.EnvironmentVariables import EnvironmentVariables
from src.event.AddUser import AddUser


class SimulationEngine:
   # environmentVariables = EnvironmentVariables.getInstance()
    #
    environmentVariables = EnvironmentVariables.getInstance()

    @staticmethod
    def createAddUserEvent():
            AddUser(
                SimulationEngine.environmentVariables.globalTime + MyRandomGenerator.RandomNumberGenerator.getRandomUserCreateTime())


