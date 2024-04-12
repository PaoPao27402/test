from facades.vacations_facades import *

with VacationFacade() as facade:

    random_vacations = facade.get_random_vacations()
    print(len(random_vacations[0]))

    facade.add_vacation()
