# pip install validate_email_address 
from email_validator import validate_email
from models.role_model import RoleModel

class UserModel:
    def __init__(self, user_ID, first_name, last_name, email, password, role_ID):
        self.user_ID = user_ID
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_ID = role_ID

    def validate_insert(self):
        if not self.first_name: return "missing first_name"
        if not self.last_name: return "missing last_name"
        if not self.email: return "missing email"
        if not self.password: return "missing password"
        if not self.role_ID: return "missing role id"
        if len(self.first_name) < 2 or len(self.first_name) > 20: return "name must be 2-20 characters"
        if len(self.last_name) < 2 or len(self.last_name) > 20: return "name must be 2-20 characters"
        if len(self.password) < 5 or len(self.password) > 255: return "password must be 5-255 characters"
        if not validate_email(self.email): return "email not valid"
        if self.role_ID != RoleModel.admin.value and self.role_ID != RoleModel.user.value: return "not valid role"
        return None
