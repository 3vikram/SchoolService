import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(user='vikram', password='Kuttyseed02022019',
                                        host='127.0.0.1', database='School')

mycursor = db_connection.cursor()

mycursor.execute("CREATE TABLE users (User_ID INT(11) AUTO_INCREMENT PRIMARY KEY, User_Name VARCHAR(255), Email_ID VARCHAR(255), User_Password VARCHAR(255), ContactNo INT(255))")
mycursor.execute("CREATE TABLE Teachers (Teacher_ID INT(11) AUTO_INCREMENT PRIMARY KEY, Teacher_Name VARCHAR(255), Teacher_Age TINYINT(255), Teacher_Qualification VARCHAR(255), Teacher_Experience INT(255), Teacher_Salary VARCHAR(255))")
mycursor.execute("CREATE TABLE Students (Student_ID INT AUTO_INCREMENT PRIMARY KEY, Student_Name VARCHAR(255), Student_Age TINYINT(255), Student_Class INT(255), Student_Section VARCHAR(255))")

'''
Modify existing table via ALTER statement

mycursor.execute("ALTER TABLE users ADD User_SessionID VARCHAR(100),Session_Flag Bool,Last_Loggedin DATETIME")

'''
