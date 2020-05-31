import re
import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(user='vikram', password='Kuttyseed02022019',
                                        host='127.0.0.1', database='School', use_pure=True)

mycursor = db_connection.cursor(prepared=True)

class UserRegistration:
    def __init__(self, Username, EmailID, Password, ConfirmPassword, contactNo):
        self.Username = Username
        self.EmailID = EmailID
        self.Password = Password
        self.ConfirmPassword = ConfirmPassword
        self.contactNo = contactNo

    def validate_Username(self):
        username_pattern = "^[a-zA-Z]+[\w]*[a-zA-Z0-9]$"
        if len(self.Username) <= 20 and re.match(username_pattern, self.Username):
            return True
        else:
            return False

    def validate_EmailID(self):
        EmailID_pattern = "^[a-zA-Z]+[\w\.]*[a-zA-Z][@*][a-zA-Z]+\.[a-z]+"
        if re.search(EmailID_pattern, self.EmailID):
            return True
        else:
            return False

    def validate_Password(self):
        self.password_min_length = 8
        self.password_max_length = 14
        if self.Password == self.ConfirmPassword and (len(self.Password) >= self.password_min_length and len(self.Password) <= self.password_max_length):
            return True
        else:
            return False

    def validate_ContactNo(self):
        if len(str(self.contactNo)) == 10 and type(self.contactNo) == int:
            return True
        else:
            return False

    def register_user(self):
        sql_query_insert = "INSERT INTO users (User_Name, Email_ID, User_Password, ContactNo) VALUES (?, ?, ?, ?)"
        sql_query_values = (self.Username, self.EmailID, self.Password, self.contactNo)
        mycursor.execute(sql_query_insert, sql_query_values)
        db_connection.commit()
        return "response: user registration is successful"

if __name__ == "__main__":
    #instance = UserRegistration("vikram", "vikram@gmail.com", "Test1212", "Test1212", 1234567890)
    pass

