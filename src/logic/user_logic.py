from utils.dal import *
from models.user_model import *

class UserLogic:
    def __init__(self):
        self.dal = DAL()

    def insert_user(self, first_name, last_name, email, password, role_ID:int):
        sql = "INSERT INTO travel_agency.users_tbl (first_name, last_name, email, password, role_ID) VALUES (%s, %s, %s, %s, %s)"
        params = (first_name, last_name, email, password, role_ID)
        result = self.dal.insert(sql, params)
        return result

    def get_user_by_mail_id(self, email, password):
        sql = "SELECT * FROM travel_agency.users_tbl WHERE email = %s AND password = %s"
        params = (email, password)
        result = self.dal.get_scalar(sql, params)
        return result

    def check_email_existence(self, email):
        sql = "SELECT COUNT(*) FROM travel_agency.users_tbl WHERE email = %s"
        params = (email,)
        result = self.dal.get_scalar(sql, params)
        return result['COUNT(*)'] > 0

    def get_all_users(self):
        sql = "SELECT * FROM travel_agency.users_tbl"
        result = self.dal.get_table(sql)
        results = UserModel.dictionaries_to_users(result)
        return results

    def get_one_user(self):
        sql = "SELECT * FROM travel_agency.users_tbl LIMIT 1"
        result = self.dal.get_table(sql)
        results = UserModel.dictionary_to_user(result)
        return results

    def register_user(self, email, password):
        if self.check_email_existence(email):
            return "Email already exists"
        elif self.is_valid_email(email) and self.is_valid_password(password):
            sql = "INSERT INTO travel_agency.users_tbl (email, password) VALUES (%s, %s)"
            params = (email, password)
            self.dal.insert(sql, params)
            return "User registered successfully ✅"
        else:
            return "Invalid email or password ❌"

    def login_user(self, email, password):
        if self.is_valid_email(email) and self.is_valid_password(password):
            sql = "SELECT COUNT(*) FROM travel_agency.users_tbl WHERE email = %s AND password = %s"
            params = (email, password)
            result = self.dal.get_scalar(sql, params)
            if result['COUNT(*)'] > 0:
                return "User logged in successfully 👌"
            else:
                return "Invalid email or password ❌"
        else:
            return "Invalid email or password 🫤"

    def is_valid_email(self, email):
        # Add email validation logic here
        return True

    def is_valid_password(self, password):
        # Add password validation logic here
        return True

    def close(self):
        self.dal.close()

