import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(user='root', password='root',
                                        host='127.0.0.1', database='school')

mycursor = db_connection.cursor()

class RetrieveTeacherInfo:

    def get_teacher_info(self, ID):
        self.ID = ID
        sql_query = "SELECT * FROM teachers WHERE Teacher_ID = {}".format(self.ID)
        mycursor.execute(sql_query)
        teacher_record = mycursor.fetchall()

        Teacher_information = {}
        for record in teacher_record:
            Teacher_information['TeacherID'] = record[0]
            Teacher_information['TeacherName'] = record[1]
            Teacher_information['TeacherAge'] = record[2]
            Teacher_information['TeacherQualification'] = record[3]
            Teacher_information['TeacherExperience'] = record[4]
            Teacher_information['TeacherSalary'] = record[5]
            return Teacher_information

if __name__ == "__main__":
    instance = RetrieveTeacherInfo()
    instance.get_teacher_info(4)

