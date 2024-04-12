from facades.vacations_facades import *
from facades.users_facades import *
from facades.users_facades import *

with VacationFacade() as facade:

    random_vacations = facade.get_random_vacations()
    print(len(random_vacations[0]))

    facade.add_vacation()
    print("A vacation has been added")

# with UsersFacade() as facade:

#     random_user = facade.get_random_user()
#     print(len(random_user[0]))

#     facade.add_vacation()
#     print("A user has been added")

#     def register(self, email):
#         facade.check_email_existence(email)

# with LikesFacade() as facade:


