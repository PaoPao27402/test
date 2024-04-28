from logic.user_logic import UserLogic
from models.user_model import UserModel

class UsersFacade:
    
    def __init__(self):
        self.logic = UserLogic()

    def register_user(self, email, password, first_name, last_name, user_ID, role_ID):

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
        result = self.logic.insert_user(first_name, last_name, email, password, user_ID, role_ID)
        if result:
            return "User registered successfully 🤓👌"
        else:
            return "Failed to register user"


    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()



