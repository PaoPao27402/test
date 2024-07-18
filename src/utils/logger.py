from datetime import datetime
from flask import session

class Logger:
    #path to log file
    __log_file = "./logger.log"

    @staticmethod
    def log(message):
        now = datetime.now()
        with open(Logger.__log_file, "a") as file: #a is for append
            file.write(str(now) + "\n")
            file.write(message + "\n")
            file.write("-------------------------------------------" + "\n")   

            #write user data if exist
            user = session.get("current_user")
            if user:
                file.write("User ID : " + str(user["id"]) + ", User Email: " + user["email"] + "\n")
            file.write("-------------------------------------------" + "\n") 



