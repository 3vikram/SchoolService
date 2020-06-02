import mysql.connector
import jwt
import datetime

db_connection = mysql.connector.connect(user='vikram', password='Kuttyseed02022019',
                                        host='db', database='School', use_pure=True)

mycursor = db_connection.cursor(prepared=True)

class UserLoginLogout:

    def login_verification(self, username, password):
        self.username = username
        self.password = password
        login_sql_query = "SELECT EXISTS(SELECT * FROM users WHERE User_Name = ? and User_Password = ?)"
        login_sql_values = (self.username, self.password)
        mycursor.execute(login_sql_query, login_sql_values)
        login_valid = mycursor.fetchall()
        if login_valid[0][0] == 1:
            secret = str(datetime.datetime.now())
            session = (jwt.encode({"username": self.username, "password": self.password}, secret , algorithm='HS256').decode())
            print(session)
            update_sql_query = "UPDATE users SET User_SessionID = ?, Session_Flag = ? WHERE User_Name = ?"
            update_sql_values = (session, True, self.username)
            mycursor.execute(update_sql_query, update_sql_values)
            db_connection.commit()
            return "response: login success, sessionID: {}".format(session)
        else:
            return "response: Invalid Credentials!"

    def logout_verification(self, sessionID):
        self.session = sessionID
        if self.session != "NULL":
            retrieve_sessionID_query = "SELECT User_Name FROM users WHERE User_SessionID = ?"
            retrieve_sessionID_value = (self.session,)
            mycursor.execute(retrieve_sessionID_query, retrieve_sessionID_value)
            logout_user_session = mycursor.fetchall()
            retrieved_username = logout_user_session[0][0]
            clear_user_session_query = "UPDATE users SET User_SessionID = ?, Session_Flag = ? WHERE User_Name = ?"
            clear_user_session_values = ("NULL", False, retrieved_username)
            mycursor.execute(clear_user_session_query, clear_user_session_values)
            db_connection.commit()
            return "response: User Successfully logged out"
        else:
            return "Invalid Operation"

if __name__ == "__main__":
    instance  = UserLoginLogout()
    #instance.login_verification('vikram', 'Test1212')
    #instance.logout_verification('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ikt1dHR5c2VlZCIsInBhc3N3b3JkIjoic21mYmFieUAxNDMifQ.NQo43lPle_BvqVQxA2Il_AqPgUgk-kHUkUckK68AYAg')
