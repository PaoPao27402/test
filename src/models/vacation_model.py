from datetime import datetime


class VacationModel:

    def __init__(self, vacations_ID, country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename):
        self.vacations_ID = vacations_ID
        self.country_ID = country_ID
        self.vacation_description = vacation_description
        self.start_vacation_date = start_vacation_date
        self.end_vacation_date = end_vacation_date
        self.price = price
        self.vacation_pic_filename = vacation_pic_filename

    def display(self):
        print(f"Vacation ID: {self.vacations_ID}\n"
              f"Country ID: {self.country_ID}\n"
              f"Vacation description: {self.vacation_description}\n"
              f"Start date: {self.start_vacation_date}\n"
              f"End date: {self.end_vacation_date}\n"
              f"The Price is: {self.price}\n"
              f"and the Vacation file is: {self.vacation_pic_filename}")

    @staticmethod
    def dictionary_to_vacation(dictionary):
        vacations_ID = dictionary["vacations_ID"]
        country_ID = dictionary["country_ID"]
        vacation_description = dictionary["vacation_description"]
        start_vacation_date = dictionary["start_vacation_date"]
        end_vacation_date = dictionary["end_vacation_date"]
        price = dictionary["price"]
        vacation_pic_filename = dictionary["vacation_pic_filename"]
        vacation = VacationModel(vacations_ID, country_ID, vacation_description, start_vacation_date, end_vacation_date, price, vacation_pic_filename)
        return vacation

    @staticmethod
    def dictionaries_to_vacations(list_of_dictionary):
        vacations = []
        for item in list_of_dictionary:
            vacation = VacationModel.dictionary_to_vacation(item)
            vacations.append(vacation)

        return vacations
    
    def validate_add_new_vacation(self):
        if not self.country_ID: 
            return "Please select country"
        if not self.vacation_description: 
            return "Please enter vacation description"
        if not self.start_vacation_date: 
            return "Please select start date"
        if not self.end_vacation_date: 
            return "Please select end date"
        if not self.price: 
            return "Please enter price"
        if not self.vacation_pic_filename: 
            return "Please select image"
        if len(self.vacation_description) < 5 or len(self.vacation_description) > 250: 
            return "Ensure the vacation description is between 5 and 250 characters"

        today = datetime.today().date()
        try:
            start = datetime.strptime(self.start_vacation_date, "%d/%m/%Y").date()  
            end = datetime.strptime(self.end_vacation_date, "%d/%m/%Y").date()      
        except ValueError:
            return "Date format should be DD/MM/YYYY"

        if start < today: 
            return "The start date cannot be a past date"
        if end < start: 
            return "The end date cannot be before the start date"
        if end < today: 
            return "The end date cannot be a past date"
        if int(self.price) < 0 or int(self.price) > 10000: 
            return "Please enter a vacation price between 0 and 10,000 nis"
        
        return None  
 
    def validate_update(self):
        if not self.country_ID: return "Please select country"
        if not self.vacation_description: return "Please enter vacation description"
        if not self.start_vacation_date: return "Please select start date"
        if not self.end_vacation_date: return "Please select end date"
        if not self.price: return "Please enter price"
        if len(self.vacation_description) < 5 or len(self.vacation_description) > 250: return "Please ensure the vacation description is up to the maximum length possible"
        start = datetime.strptime(self.start_vacation_date, "%d-%m-%Y").date()
        end = datetime.strptime(self.end_vacation_date, "%d-%m-%Y").date()
        if end < start: return "The end date cannot be before the start date"
        if int(self.price) < 0 or int(self.price) > 10000: return "Please enter a vacation price between 0 and 10,000 nis"
        return None



