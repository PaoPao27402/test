from utils.dal import *
from models.vacation_model import *

class VacationLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_vacations(self):
        sql = "SELECT * FROM travel_agency.vacations_tbl"
        result = self.dal.get_table(sql)
        results = VacationModel.dictionaries_to_vacations(result)

        return results
    
    def get_one_vacation(self):
        sql = "SELECT * FROM travel_agency.vacations_tbl LIMIT 1"
        result = self.dal.get_table(sql)
        results = VacationModel.dictionary_to_vacation(result)
        
        return results
    
    def add_vacation(self, vacations_ID, country_ID, vacation_description, start_vacation_date, end_vacation_date, price):
        sql = "INSERT INTO travel_agency.vacations_tbl (vacation_ID, country_ID, vacations_description, start_vacation_date, end_vacation_date, price) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (vacations_ID, country_ID, vacation_description, start_vacation_date, end_vacation_date, price)
        result = self.dal.insert(sql, params)

        return result

    def update_vacation(self, vacations_ID, country_ID, start_vacation_date, end_vacation_date, price):
        sql = "UPDATE travel_agency.vacations_tbl SET country_ID = %s, start_vacation_date = %s, end_vacation_date = %s, price = %s WHERE vacations_ID = %s"
        params = (vacations_ID, start_vacation_date, end_vacation_date, price, country_ID)
        result = self.dal.update(sql, params)
        return result

    def delete_vacation(self, vacations_ID):
        sql = "DELETE FROM travel_agency.vacations_tbl WHERE vacations_ID = %s"
        params = (vacations_ID,)
        result = self.dal.delete(sql, params)

        return result
    
    def close(self):
        self.dal.close()