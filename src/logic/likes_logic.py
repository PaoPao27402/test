from utils.dal import *
from models.likes_model import *

class LikesLogic:
    def __init__(self):
        self.dal = DAL()

    def add_vacation_like(self, user_ID, vacations_ID):
        sql = "INSERT INTO travel_agency.likes_table (user_ID, vacations_ID) VALUES (%s, %s)"
        params = (user_ID, vacations_ID)
        result = self.dal.insert(sql, params)
        return result

    def delete_vacation_like(self, user_ID, vacations_ID):
        sql = "DELETE FROM travel_agency.likes_table WHERE user_ID = %s AND vacations_ID = %s"
        params = (user_ID, vacations_ID)
        result = self.dal.delete(sql, params)
        return result
    
    

    def close(self):
        self.dal.close()
          
