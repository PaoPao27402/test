from utils.dal import DAL
from models.vacation_model import VacationModel
from utils.image_handler import ImageHandler 

class VacationLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_vacations(self):
        sql = "SELECT v.vacations_ID, v.country_ID, v.vacation_description, v.start_vacation_date, v.end_vacation_date, v.price, v.vacation_pic_filename, c.country_name FROM travel_agency.vacations_tbl v JOIN travel_agency.countries_tbl c ON v.country_ID = c.country_ID"
        results = self.dal.get_table(sql)
        return VacationModel.dictionaries_to_vacations(results)


    def get_one_vacation(self, vacations_ID):
        sql = "SELECT v.vacations_ID, v.country_ID, v.vacation_description, v.start_vacation_date, v.end_vacation_date, v.price, v.vacation_pic_filename, c.country_name FROM travel_agency.vacations_tbl v JOIN travel_agency.countries_tbl c ON v.country_ID = c.country_ID WHERE v.vacations_ID = %s"
        result = self.dal.get_scalar(sql, (vacations_ID,))
        if result:
            return VacationModel.dictionary_to_vacation(result)
        return None

    def add_vacation(self, country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename):
        vacation_pic_filename = ImageHandler.save_image(vacation_pic_filename)
        sql = "INSERT INTO travel_agency.vacations_tbl (country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename)
        return self.dal.insert(sql, params)

    def update_vacation(self, vacations_ID, country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename):
        old_image_name = self.get_old_image_name(vacations_ID)
        vacation_pic_filename = ImageHandler.update_image(old_image_name, vacation_pic_filename)
        sql = "UPDATE travel_agency.vacations_tbl SET country_ID = %s, vacation_description = %s, start_vacation_date = %s, end_vacation_date = %s, price = %s, vacation_pic_filename = %s WHERE vacations_ID = %s"
        params = (country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename, vacations_ID) 
        return self.dal.update(sql, params)


    def get_all_countries_order_by_name(self):
        sql = "SELECT country_ID, country_name FROM countries_tbl ORDER BY country_name"
        return self.dal.get_table(sql)

    def get_country_name(self, country_ID):
        sql = "SELECT country_name FROM countries_tbl WHERE country_ID = %s"
        result = self.dal.get_scalar(sql, (country_ID,))
        return result['country_name'] if result else None  

    def delete_vacation(self, vacations_ID):
        # Delete likes associated with the vacation
        sql_likes = "DELETE FROM travel_agency.likes_tbl WHERE vacations_ID = %s"
        self.dal.delete(sql_likes, (vacations_ID,))

        # Delete the vacation image
        image_name = self.get_old_image_name(vacations_ID)
        ImageHandler.delete_image(image_name)

        # Delete the vacation
        sql_vacation = "DELETE FROM travel_agency.vacations_tbl WHERE vacations_ID = %s"
        self.dal.delete(sql_vacation, (vacations_ID,))
        return "Vacation deleted successfully"
    
    def get_old_image_name(self, vacations_ID):
        sql = "SELECT vacation_pic_filename FROM travel_agency.vacations_tbl WHERE vacations_ID = %s"
        result = self.dal.get_scalar(sql, (vacations_ID,))
        return result["vacation_pic_filename"]
    
    def close(self):
        self.dal.close()
