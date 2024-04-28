from utils.dal import *
from models.vacation_model import *
from datetime import datetime

class VacationLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_vacations(self):
        sql = "SELECT * FROM travel_agency.vacations_tbl ORDER BY start_vacation_date ASC"
        result = self.dal.get_table(sql)
        results = VacationModel.dictionaries_to_vacations(result)
        return results

    def add_vacation(self, country_ID, start_vacation_date, end_vacation_date, price):
        if self.is_valid_date(start_vacation_date) and self.is_valid_date(end_vacation_date) and 0 <= price <= 10000:
            if start_vacation_date <= end_vacation_date:
                sql = "INSERT INTO travel_agency.vacations_tbl (country_ID, start_vacation_date, end_vacation_date, price) VALUES (%s, %s, %s, %s)"
                params = (country_ID, start_vacation_date, end_vacation_date, price)
                self.dal.insert(sql, params)
                return "Vacation added successfully 🎊"
            else:
                return "Invalid input: End date cannot be earlier than start date"
        else:
            return "Invalid input for vacation 😑"

    def update_vacation(self, vacations_ID, country_ID, start_vacation_date, end_vacation_date, price):
        if self.is_valid_date(start_vacation_date) and self.is_valid_date(end_vacation_date) and 0 <= price <= 10000:
            if start_vacation_date <= end_vacation_date:
                sql = "UPDATE travel_agency.vacations_tbl SET country_ID = %s, start_vacation_date = %s, end_vacation_date = %s, price = %s WHERE vacation_ID = %s"
                params = (country_ID, start_vacation_date, end_vacation_date, price, vacations_ID)
                self.dal.update(sql, params)
                return "Vacation updated successfully 🎉"
            else:
                return "Invalid input: End date cannot be earlier than start date"
        else:
            return "Invalid input for vacation 😑"

    def delete_vacation(self, vacations_ID):
        # Delete likes associated with the vacation
        sql_likes = "DELETE FROM travel_agency.likes_tbl WHERE vacation_ID = %s"
        self.dal.delete(sql_likes, (vacations_ID,))

        # Delete the vacation
        sql_vacation = "DELETE FROM travel_agency.vacations_tbl WHERE vacation_ID = %s"
        self.dal.delete(sql_vacation, (vacations_ID,))
        return "Vacation deleted successfully 🗑️"

    def is_valid_date(self, date_str):
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            return date >= datetime.now()
        except ValueError:
            return False

    def close(self):
        self.dal.close()

