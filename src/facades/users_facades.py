import random
from logic.user_logic import UserLogic
from models.user_model import UserModel

class UsersFacade:
    
    def __init__(self):
        self.logic = UserLogic()

    def register_user(self, email, password, first_name, last_name):

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
        user = UserModel(email=email, password=password, first_name=first_name, last_name=last_name)
        self.logic.insert_user(user)
        return "User registered successfully 🤓👌"
        
    def sign_in(self, email, password):
        # Validate email and password
        if not self.logic.is_valid_email(email):
            return "Invalid email format 😑"
        if len(password) < 4:
            return "Password must be at least 4 characters long"

        # Check if user exists
        user = self.logic.get_user_by_mail_id(email)
        if user:
            if user.password == password:
                return "Sign-in successful ✅"
            else:
                return "Incorrect password"
        else:
            return "User does not exist"

    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()



