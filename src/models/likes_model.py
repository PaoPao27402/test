class LikeModel:

        def __init__(self, user_ID, vacations_ID):
                self.user_ID = user_ID
                self.vacations_ID = vacations_ID

        def display(self):
                print(f"User: {self.user_ID} Liked: {self.vacations_ID}")

        @staticmethod
        def dictionary_to_like(dictionary):
            vacations_ID = dictionary["vacations_ID"]
            user_ID = dictionary["user_ID"]
            like = LikeModel(vacations_ID, user_ID)
            return like
        
        @staticmethod
        def dictionaries_to_likes(list_of_likes_dict):
            likes = []
            for item in list_of_likes_dict:
                like = LikeModel.dictionary_to_like(item)
                likes.append(like)
            return likes
    


