from facades.vacations_facades import *
from facades.users_facades import *
from facades.likes_facades import *

class Test:
    def __init__(self):
        self.vacation_facade = VacationFacade()
        self.users_facade = UsersFacade()
        self.likes_facade = LikesFacade()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.vacation_facade.close()
        self.users_facade.close()
        self.likes_facade.close()

    def test_vacation_facade(self):
        print("Testing Vacation Facade...")

        with self.vacation_facade as facade:
            # Test get_random_vacations
            random_vacations = facade.get_random_vacations()
            print("Random Vacations:", random_vacations)

            # Test add_vacation (assuming parameters are provided)
            result = facade.add_vacation(country_ID="Country", start_vacation_date="2024-05-01", end_vacation_date="2024-05-10", price=1000)
            print("Add Vacation Result:", result)

    def test_users_facade(self):
        print("Testing Users Facade...")
  
        with self.users_facade as facade:
        # Test get_random_user
            random_user = facade.get_random_user()
            print("Random User Details:")
            print("First Name:", random_user.first_name)
            print("Last Name:", random_user.last_name)
            print("Email:", random_user.email)

    def test_likes_facade(self):
        print("Testing Likes Facade...")
       
        with self.likes_facade as facade:
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




