class ClientError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message 

class ResourceNotFoundError(ClientError):
    def __init__(self, user_ID): 
        super().__init__(f"{user_ID} not found 🔎")
        self.id = user_ID 

class ValidationError(ClientError):
    def __init__(self, message, model):
        super().__init__(message)
        self.model = model 

class AuthError(ClientError):
    def __init__(self, message, model=None):
        super().__init__(message)
        self.model = model




