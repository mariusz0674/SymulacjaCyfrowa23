from src.EnviromentalVariables import EnviromentalVariables
from src.User import User


class SimulationEngine:
    enviromentalVariables = None

    @staticmethod
    def init(env_vars: EnviromentalVariables):
        SimulationEngine.enviromentalVariables = env_vars

    @staticmethod
    def createUser():
        SimulationEngine.enviromentalVariables.usersCounter += 1
        return User(
            SimulationEngine.enviromentalVariables.usersCounter,
            1,
        )
