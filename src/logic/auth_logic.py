from utils.dal import DAL 

class AuthLogic:
    def __init__(self) -> None:
        self.dal = DAL() 

    def add_user(self, user):
        sql = "INSERT INTO users(first_name, last_name, email, password, role_id) VALUES(%s, %s, %s,%s, %s)"
        self.dal.insert(sql , (user.first_name, user.last_name, user.email, user.password, user.role_id))


    def is_email_taken(self, email):
        sql  = "select EXISTS(select *from users where email = %s) as is_taken"
        result = self.dal.get_scalar(sql, (email,))
        return result["is_taken"] == 1 
    
    def get_user(self, credentials):
        sql = "SELECT * FROM users where email = %s and password = %s"
        user = self.dal.get_scalar(sql, (credentials.email, credentials.password))
        return user

    def close(self):
        self.dal.close(); 


