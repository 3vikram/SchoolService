import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(user='root', password='root',
                                        host='127.0.0.1', database='school')

mycursor = db_connection.cursor()

class RetrieveStudentInfo:

    def get_student_info(self, ID):
        self.ID = ID
        sql_query = "SELECT * FROM students WHERE Student_ID = {}".format(self.ID)
        mycursor.execute(sql_query)
        student_record = mycursor.fetchall()

        Student_information = {}
        for record in student_record:
            Student_information['studentID'] = record[0]
            Student_information['studentName'] = record[1]
            Student_information['studentAge'] = record[2]
            Student_information['studentClass'] = record[3]
            Student_information['studentSection'] = record[4]
            return Student_information


if __name__ == "__main__":
    instance = RetrieveStudentInfo()
    instance.get_student_info(4)

