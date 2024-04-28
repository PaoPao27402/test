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
            result = facade.add_vacation(vacations_ID=98, country_ID=6, vacation_description="Amazing beaches", start_vacation_date="2028-08-16", end_vacation_date="2028-09-28", price=600, vacation_pic_filename = "vac_pic_11")
            print("Add Vacation Result:", result)

    def test_users_facade(self):
        print("Testing Users Facade...")

        # Hard-coded user registration
        registration_result = self.users_facades.register_user(
            email="davetonny@example.com",
            password="p$2222word123",
            first_name="Tonny",
            last_name="Dave",
            user_ID="UI08",  
            role_ID=2   
        )
        print("Registration Result:", registration_result)

        # Hard-coded user sign-in
        sign_in_result = self.users_facades.register_user(
            email="test@example.com",
            password="password123"
        )
        print("Sign-in Result:", sign_in_result)

    def test_likes_facade(self):
        print("Testing Likes Facade...")
       
        with self.likes_facades as facade:
            # Test add_vacation_like (assuming parameters are provided)
            result = facade.add_vacation_like(user_ID="UI07", vacations_ID=10)
            print("Add Like Result:", result)

            # Test delete_vacation_like (assuming parameters are provided)
            result = facade.delete_vacation_like(user_ID="UI07", vacations_ID=2)
            print("Delete Like Result:", result)

    def test_all(self):
        self.test_vacation_facade()
        self.test_users_facade()
        self.test_likes_facade()

with Test() as test_instance:
    test_instance.test_all()





