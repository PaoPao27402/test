from logic.likes_logic import LikesLogic

class LikesFacade:
    
    def __init__(self):
        self.logic = LikesLogic()
    
    def like_vacation(self, user_ID, vacations_ID):
        return self.logic.add_vacation_like(user_ID, vacations_ID)

    def unlike_vacation(self, user_ID, vacations_ID):
        return self.logic.delete_vacation_like(user_ID, vacations_ID)

    def close(self):
        self.logic.close()

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()