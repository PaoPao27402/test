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

    def add_vacation(self, country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename, country_name):
        new_vacation = VacationModel(None, country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename, country_name)
        error = new_vacation.validate_add_new_vacation()
        if error:
            raise ValidationError(error, new_vacation)
        self.logic.add_vacation(new_vacation.country_ID, new_vacation.vacation_description, new_vacation.start_vacation_date, new_vacation.end_vacation_date, new_vacation.price, new_vacation.vacation_pic_filename)

    def update_vacation(self, vacations_ID):
        existing_vacation = self.logic.get_one_vacation(vacations_ID)
        if not existing_vacation:
            raise ValidationError("Vacation not found", None)
        
        vacation_description = request.form.get("vacation_description")
        start_vacation_date = request.form.get("start_vacation_date")
        end_vacation_date = request.form.get("end_vacation_date")
        price = request.form.get("price")
        vacation_pic_filename = request.files.get("image")
        
        # Fetch country_name from your data source
        country_name = self.get_country_name(existing_vacation.country_ID)
        
        vacation_model = VacationModel(
            vacations_ID=vacations_ID,
            country_ID=existing_vacation.country_ID,
            vacation_description=vacation_description,
            start_vacation_date=start_vacation_date,
            end_vacation_date=end_vacation_date,
            price=price,
            vacation_pic_filename=vacation_pic_filename,
            country_name=country_name
        )

        if not all([vacation_description, start_vacation_date, end_vacation_date, price]):
            raise ValidationError("All fields must be filled", vacation_model)
        return self.logic.update_vacation(vacations_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename)


    def delete_vacation(self, vacations_ID):
        return self.logic.delete_vacation(vacations_ID)

    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()




