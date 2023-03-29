import User
from EnviromentalVariables import EnviromentalVariables
class SimulationEngine:
    def __init__(self,
                 enviromentalVariables: EnviromentalVariables,
                 ):
        self.enviromentalVariables = enviromentalVariables

    
    def createUser(self):
        self.enviromentalVariables.usersCounter+=1
        return User(self.enviromentalVariables.usersCounter,
                    1,
                    )
