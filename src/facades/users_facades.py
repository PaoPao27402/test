from logic.user_logic import *
from models.user_model import *

class UsersFacade:
    
    def __init__(self):
        self.logic = UserLogic()

    def register_user(self, user_ID, first_name, last_name, email, password, role_ID):

        if not self.logic.is_valid_email(email):
            return "Invalid email format 😑"

        # Password meets minimum length requirement
        if len(password) < 4:
            return "Password must be at least 4 characters long"

        # Checking if email already exists in the system
        if self.logic.check_email_existence(email):
            return "Email already exists in the system"
        
        # Check if first name and last name are provided
        if not first_name:
            return "Must enter a First Name"
        
        if not last_name:
            return "Must enter a Last Name"
        
        # Add user to the system
        result = self.logic.insert_user(user_ID, first_name, last_name, email, password, role_ID)
        if result:
            return "User registered successfully 🤓👌"
        else:
            return "Failed to register user 🫤"
        
    def login_user(self, email, password):
    # Perform email format validation
        if not self.logic.is_valid_email(email):
            raise ValueError("Invalid email format 😑")
    
    # Perform password length validation
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long")

    # Retrieve user by email and password
        user = self.logic.get_user_by_email_and_pass(email, password)
    
        if not user:
            raise ValueError("Email or password are incorrect")
        
        else:
            self.roleId = user["roleId"]
            print("Email and Password match, Signed in")
        return user

    def role(self):
        if hasattr(self, 'roleId') and self.roleId != 0:

            return self.roleId
        
        else:
         raise ValueError("No user is connected")



    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

