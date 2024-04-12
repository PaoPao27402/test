import random
from logic.likes_logic import *
from models.likes_model import *

class LikesFacade:
    
    def __init__(self):
        self.logic = LikesLogic()

    # def get_random_like(self):
    #     all_likes = self.logic.get_all_users()
    #     index = random.randint(0, len(all_users) - 1)
    #     random_user = all_users[index]

    #     return random_user
    
    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()