class UserModel:

    def __init__(self, user_ID, first_name, last_name, email, password, role_ID):
        self.user_ID = user_ID
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_ID = role_ID

    def display(self):
        print(f"User ID: {self.user_ID} First Name: {self.first_name} Last Name: {self.last_name} Email: {self.email} Password: {self.password} Role ID: {self.role_ID}")


    @staticmethod
    def dictionary_to_user(dictionary):
        user_ID = dictionary["user_ID"]
        first_name = dictionary["first_name"]
        last_name = dictionary["last_name"]
        email = dictionary["email"]
        password = dictionary["password"]
        role_ID = dictionary["role_ID"]
        user = UserModel(user_ID, first_name, last_name, email, password, role_ID)
        return user
    
    @staticmethod
    def dictionaries_to_user(dictionary_list):
        users = []
        for item in dictionary_list:
            user = UserModel.dictionary_to_user(item)
            users.append(user)

        return users