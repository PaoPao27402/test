import random
from logic.vacation_logic import *
from models.vacation_model import *

class VacationFacade:
    
    def __init__(self):
        self.logic = VacationLogic()

    def get_random_vacations(self):
        all_vacations = self.logic.get_all_vacations()
        index = random.randint(0, len(all_vacations) - 1)
        random_vacations = all_vacations[index]

        return random_vacations
    
    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()




