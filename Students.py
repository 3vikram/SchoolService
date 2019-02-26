import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(user='root', password='root',
                                        host='127.0.0.1', database='school', use_pure=True)

mycursor = db_connection.cursor(prepared=True)

class RetrieveStudentInfo:

    def get_student_info(self, ID):
        self.ID = ID
        sql_query = "SELECT * FROM students WHERE Student_ID = ?"
        sql_value = (self.ID,)
        mycursor.execute(sql_query, sql_value)
        student_record = mycursor.fetchall()

        Student_information = {}
        for record in student_record:
            Student_information['studentID'] = record[0]
            Student_information['studentName'] = record[1]
            Student_information['studentAge'] = record[2]
            Student_information['studentClass'] = record[3]
            Student_information['studentSection'] = record[4]
        return Student_information

    def set_student_info(self, name, age, sclass, section):
        self.name = name
        self.age = age
        self.Class = sclass
        self.section = section

        sql_query_insert = "INSERT INTO students (Student_Name, Student_Age, Student_Class, Student_Section) VALUES (?, ?, ?, ?)"
        sql_query_values = (self.name, self.age, self.Class, self.section)
        mycursor.execute(sql_query_insert, sql_query_values)
        db_connection.commit()

        return "response: successfully created student in the database"

    def get_total_students(self):
        sql_query = "SELECT count(*) FROM students"
        mycursor.execute(sql_query)
        total_students = mycursor.fetchall()
        return "Total Students: {}".format(total_students[0][0])

    def remove_student(self, ID):
        self.ID = ID
        sql_query = "DELETE FROM students WHERE Student_ID=?"
        sql_value = (self.ID,)
        mycursor.execute(sql_query, sql_value)
        db_connection.commit()
        return "Successfully removed student data"

    def update_student_info(self, name, age, Class, section):
        self.name = name
        self.age = age
        self.Class = Class
        self.section = section
        sql_query_update = "UPDATE students SET Student_Age = ?, Student_Class = ?, Student_Section = ? WHERE Student_Name = ?"
        sql_query_update_values = (self.age, self.Class, self.section, self.name)
        mycursor.execute(sql_query_update, sql_query_update_values)
        db_connection.commit()
        return "Success: Updated student {} record in our database".format(self.name)


if __name__ == "__main__":
    instance = RetrieveStudentInfo()
