import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(user='root', password='root',
                                        host='127.0.0.1', database='school', use_pure=True)

mycursor = db_connection.cursor(prepared=True)

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

    def set_teacher_info(self, name, age, qualification, experience, salary):
        self.name = name
        self.age = age
        self.qualification = qualification
        self.experience = experience
        self.salary = salary
        sql_query_insert = "INSERT INTO teachers (Teacher_Name, Teacher_Age, Teacher_Qualification, Teacher_Experience, Teacher_Salary) VALUES (?, ?, ?, ?, ?)"
        sql_query_values = (self.name, self.age, self.qualification, self.experience, self.salary)
        mycursor.execute(sql_query_insert, sql_query_values)
        db_connection.commit()

        return "response: successfully created teacher in the database"

    def get_total_teachers(self):
        sql_query = "SELECT count(*) FROM teachers"
        mycursor.execute(sql_query)
        total_teachers = mycursor.fetchall()
        return "Total Teachers: {}".format(total_teachers[0][0])

    def remove_teacher(self, ID):
        self.ID = ID
        sql_query = "DELETE FROM teachers WHERE Teacher_ID={}".format(self.ID)
        mycursor.execute(sql_query)
        db_connection.commit()
        return "Successfully removed teacher data"


if __name__ == "__main__":
    instance = RetrieveTeacherInfo()
    instance.get_teacher_info(4)
    instance.get_total_teachers()

