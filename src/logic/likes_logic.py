from utils.dal import *
from models.likes_model import *

class LikesLogic:
    def __init__(self):
        self.dal = DAL()
        
    def add_vacation_like(self, user_ID, vacations_ID):
        # Check if user_ID exists
        if not self.user_exists(user_ID):
            return "User does not exist"

        # Check if vacations_ID exists
        if not self.vacation_exists(vacations_ID):
            return "Vacation does not exist"

        # If both user and vacation exist, proceed to add like
        sql = "INSERT INTO travel_agency.likes_table (user_ID, vacations_ID) VALUES (%s, %s)"
        params = (user_ID, vacations_ID)
        result = self.dal.insert(sql, params)
        return result
    
    def user_exists(self, user_ID):
        sql = "SELECT COUNT(*) FROM travel_agency.users_tbl WHERE user_ID = %s"
        params = (user_ID,)
        result = self.dal.get_scalar(sql, params)
        return result['COUNT(*)'] > 0

    def vacation_exists(self, vacations_ID):
        sql = "SELECT COUNT(*) FROM travel_agency.vacations_tbl WHERE vacations_ID = %s"
        params = (vacations_ID,)
        result = self.dal.get_scalar(sql, params)
        return result['COUNT(*)'] > 0

    def delete_vacation_like(self, user_ID, vacations_ID):
        # Check if the like entry exists before attempting to delete it
        if not self.like_exists(user_ID, vacations_ID):
            return "Like entry does not exist"

        # If the like entry exists, proceed to delete it
        sql = "DELETE FROM travel_agency.likes_table WHERE user_ID = %s AND vacations_ID = %s"
        params = (user_ID, vacations_ID)
        result = self.dal.delete(sql, params)
        return result

    def like_exists(self, user_ID, vacations_ID):
        sql = "SELECT COUNT(*) FROM travel_agency.likes_table WHERE user_ID = %s AND vacations_ID = %s"
        params = (user_ID, vacations_ID)
        result = self.dal.get_scalar(sql, params)
        return result['COUNT(*)'] > 0
    

    def close(self):
        self.dal.close()
          
