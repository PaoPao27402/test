class LikeModel:

        def __init__(self, user_ID, vacations_ID):
                self.user_ID = user_ID
                self.vacations_ID = vacations_ID

        def display(self):
                print(f"User: {self.user_ID} Liked: {self.vacations_ID}")

