from src import MyRandomGenerator
from src.EnvironmentVariables import EnvironmentVariables
from src.User import User
from src.event.AddUser import AddUser


class SimulationEngine:
   # environmentVariables = EnvironmentVariables.getInstance()
    #
    environmentVariables = EnvironmentVariables.getInstance()

    @staticmethod
    def createAddUserEvent():
            AddUser(
                SimulationEngine.environmentVariables.globalTime + MyRandomGenerator.RandomNumberGenerator.get_random_number())


