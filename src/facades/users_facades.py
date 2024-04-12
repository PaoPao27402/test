import random
from logic.user_logic import *
from models.user_model import *

class UsersFacade:
    
    def __init__(self):
        self.logic = UserLogic()

    def get_random_user(self):
        all_users = self.logic.get_all_users()
        index = random.randint(0, len(all_users) - 1)
        random_user = all_users[index]

        return random_user
    
    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()