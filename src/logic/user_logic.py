from utils.dal import *
from models.user_model import *

class UserLogic:
    def __init__(self):
        self.dal = DAL()

    def insert_user(self,first_name, last_name, email, password, role_ID:int):
        sql = "INSERT INTO travel_agency.users_tbl (first_name, last_name, email, password, role_ID) VALUES (%s, %s, %s, %s, %s)"
        params = (first_name, last_name, email, password, role_ID)
        result = self.dal.insert(sql, params)
        results = UserModel.dictionaries_to_users(result)  # convert dict to object

        return results

    def get_all_users(self):
        sql = "SELECT * FROM travel_agency.users_tbl"
        result = self.dal.get_table(sql)
        results = UserModel.dictionaries_to_users(result) # convert dict to object
        
        return results
    
    def get_one_user(self):
        sql = "SELECT * FROM travel_agency.users_tbl limit 1"
        result = self.dal.get_table(sql)
        results = UserModel.dictionary_to_user(result) # convert dict to object
        
        return results
    
    def close(self):
        self.dal.close()

user = UserLogic()
user.insert_user("yoel","mizrahi","yoel@intel.com","12345",2)