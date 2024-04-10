from utils.dal import *
from models.user_model import *

class UserLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_users(self):
        sql = "SELECT * FROM travel_agency.users_tbl"
        result = self.dal.get_table(sql)
        results = UserModel.dictionaries_to_user(result) # convert dict to object
        
        return results
    
    def get_one_user(self):
        sql = "SELECT * FROM travel_agency.users_tbl limit 1"
        result = self.dal.get_table(sql)
        results = UserModel.dictionary_to_user(result) # convert dict to object
        
        return results
    
    def close(self):
        self.dal.close()