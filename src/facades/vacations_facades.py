from logic.vacation_logic import VacationLogic
from models.vacation_model import *
from models.client_error import ValidationError
from utils.image_handler import *
from flask import request

class VacationFacade:
    
    def __init__(self):
        self.logic = VacationLogic()

    def get_all_vacations(self):
        return self.logic.get_all_vacations()
    
    def get_one_vacation(self, vacations_ID):
        return self.logic.get_one_vacation(vacations_ID)

    def add_vacation(self, country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename):
        country_ID = request.form.get("country")
        vacation_description = request.form.get("description")
        start_vacation_date = request.form.get("start_date")
        end_vacation_date = request.form.get("end_date")
        price = request.form.get("price")
        vacation_pic_filename = request.files.get["image"]
        new_vacation = VacationModel(None, country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename)
        error = new_vacation.validate_add_new_vacation()
        if error: raise ValidationError(error, new_vacation) 
        self.logic.add_vacation(new_vacation)
        

    
    def update_vacation(self, vacations_ID, country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename):
        vacations_ID = request.form.get("vacations_ID")
        country_ID = request.form.get("country_ID")
        vacation_description = request.form.get("vacation_description")
        start_vacation_date = request.form.get("start_vacation_date")
        end_vacation_date = request.form.get("end_vacation_date")
        price = request.form.get("price")
        vacation_pic_filename = request.files["vacation_pic_filename"]
        return self.logic.update_vacation(vacations_ID, country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename)

    def delete_vacation(self, vacations_ID):
        return self.logic.delete_vacation(vacations_ID)

    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()




