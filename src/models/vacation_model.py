class VacationModel:

    def __init__(self, vacations_ID, country_ID, vacation_description, start_vacation_date, end_vacation_date, price):
        self.vacations_ID = vacations_ID
        self.country_ID = country_ID
        self.vacation_description = vacation_description
        self.start_vacation_date = start_vacation_date
        self.end_vacation_date = end_vacation_date
        self.price = price

    def display(self):
        print(f"Vacation ID: {self.vacations_ID} 
              Country ID: {self.country_ID} 
              Vacation description: {self.vacation_description} 
              Start date: {self.start_vacation_date} 
              End date{self.end_vacation_date} 
              and the Price is: {self.price}")
        
    @staticmethod
    def dictionary_to_vacation(dictionary):
        vacations_ID = dictionary["vacations_ID"]
        country_ID = dictionary["country_ID"]
        vacation_description = dictionary["vacation_description"]
        start_vacation_date = dictionary["start_vacation_date"]
        end_vacation_date = dictionary["end_vacation_date"]
        price = dictionary["price"]
        vacation = VacationModel(vacations_ID, country_ID, vacation_description, start_vacation_date, end_vacation_date, price)
        return vacation
    
    @staticmethod
    def dictionaries_to_vacation(list_of_dictionary):
        payments = []
        for item in list_of_dictionary:
            payment = VacationModel.dictionary_to_payment(item)
            payments.append(payment)

        return payments
