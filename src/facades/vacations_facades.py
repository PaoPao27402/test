from logic.vacation_logic import *
from models.vacation_model import *

class VacationFacade:
    
    def __init__(self):
        self.logic = VacationLogic()

    def get_all_vacations(self):
        return self.logic.get_all_vacations()

    def add_vacation(self, vacations_ID, country_ID, start_vacation_date, end_vacation_date, price):
        return self.logic.add_vacation(vacations_ID, country_ID, start_vacation_date, end_vacation_date, price)
    
    def update_vacation(self, vacations_ID, country_ID, start_vacation_date, end_vacation_date, price):
        return self.logic.update_vacation(vacations_ID, country_ID, start_vacation_date, end_vacation_date, price)

    def delete_vacation(self, vacations_ID):
        return self.logic.delete_vacation(vacations_ID)

    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()




