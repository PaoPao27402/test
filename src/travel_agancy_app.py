from facades.vacations_facades import *
from facades.users_facades import *
from facades.likes_facades import *

class Test:
    def __init__(self):
        self.vacations_facades = VacationFacade()
        self.users_facades = UsersFacade()
        self.likes_facades = LikesFacade()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.vacations_facades.close()
        self.users_facades.close()
        self.likes_facades.close()

    def test_vacation_facade(self):
        print("Testing Vacation Facade...")

        with self.vacations_facades as facade:
            # Test get_random_vacations
            random_vacations = facade.get_all_vacations()
            print("Random Vacations:", random_vacations)

            # Test add_vacation (assuming parameters are provided)
            result = facade.add_vacation(country_ID="8", start_vacation_date="14/05/2028", end_vacation_date="18/06/2028", price= 500)
            print("Add Vacation Result:", result)

    def test_users_facade(self):
        print("Testing Users Facade...")
  
        with self.users_facades as facade:
        # Test get_random_user
            random_user = facade.get_random_user()
            print("Random User Details:")
            print("First Name:", random_user.first_name)
            print("Last Name:", random_user.last_name)
            print("Email:", random_user.email)

    def test_likes_facade(self):
        print("Testing Likes Facade...")
       
        with self.likes_facades as facade:
            # Test add_vacation_like (assuming parameters are provided)
            result = facade.add_vacation_like(user_ID=1, vacations_ID=1)
            print("Add Like Result:", result)

            # Test delete_vacation_like (assuming parameters are provided)
            result = facade.delete_vacation_like(user_ID=1, vacations_ID=1)
            print("Delete Like Result:", result)

    def test_all(self):
        self.test_vacation_facade()
        self.test_users_facade()
        self.test_likes_facade()

with Test() as test_instance:
    test_instance.test_all()




