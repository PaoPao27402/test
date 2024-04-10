from utils.dal import *
from models.vacation_model import *

class VacationLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_vacations(self):
        sql = "SELECT * FROM travel_agency.users_tbl"
        result = self.dal.get_table(sql)
        results = VacationModel.dictionaries_to_vacations(result) # convert dict to object
        
        return results
    
    def get_one_vacation(self):
        sql = "SELECT * FROM travel_agency.users_tbl limit 1"
        result = self.dal.get_table(sql)
        results = VacationModel.dictionary_to_vacation(result) # convert dict to object
        
        return results
    
    def close(self):
        self.dal.close()