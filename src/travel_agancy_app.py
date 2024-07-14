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
            # Test get_all_vacations
            all_vacations = facade.get_all_vacations()
            print("All Vacations:", all_vacations)

            # Test add_vacation (assuming parameters are provided)
            result = facade.add_vacation(vacations_ID=27, country_ID=10, vacation_description="Tour in the forest and rain", start_vacation_date="2029-12-18", end_vacation_date="2029-12-28", price=891, vacation_pic_filename = "vac_pic_11")
            print("Add Vacation Result:", result)

    def test_users_facade(self):
        print("Testing Users Facade...")
        
        # Test user registration
        user_ID = "UI17"
        first_name = "Paul"
        last_name = "Henry"
        email = "paul.henry@example.com"
        password = "12pass"
        role_ID = "2"

        registration_result = self.users_facades.register_user(user_ID, first_name, last_name, email, password, role_ID)
        print(f"Registration Result: {registration_result}")

    def test_login_user_facade(self):
        print("Testing Users sign in...")

        email = "jhondoe@example.com",
        password ="password123"

        sign_in_result = self.users_facades.login_user(email, password)
        print("Sign-in Result:", sign_in_result)


    def test_likes_facade(self):
        print("Testing Likes Facade...")
   
        with self.likes_facades as facade:
            result_1 = facade.add_vacation_like(user_ID="UI04", vacations_ID=18)
            print("Add Like Result:", result_1)

            result_2 = facade.delete_vacation_like(user_ID="UI09", vacations_ID=48)
            print("Delete Like Result:", result_2)

    def test_all(self):
        self.test_vacation_facade()
        self.test_users_facade()
        self.test_likes_facade()

with Test() as test_instance:
    test_instance.test_all()





