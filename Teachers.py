import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(user='vikram', password='Kuttyseed02022019',
                                        host='db', database='School', use_pure=True)

mycursor = db_connection.cursor(prepared=True)

class RetrieveTeacherInfo:

    def get_teacher_info(self, ID):
        self.ID = ID
        sql_query = "SELECT * FROM teachers WHERE Teacher_ID = ?"
        sql_value = (self.ID,)
        mycursor.execute(sql_query, sql_value)
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
        sql_query = "DELETE FROM teachers WHERE Teacher_ID=?"
        sql_value = (self.ID,)
        mycursor.execute(sql_query, sql_value)
        db_connection.commit()
        return "Successfully removed teacher data"

    def update_teacher_info(self, name, age, qualification, experience, salary):
        self.name = name
        self.age = age
        self.qualification = qualification
        self.experience = experience
        self.salary = salary
        sql_query_update = "UPDATE teachers SET Teacher_Age = ?, Teacher_Qualification = ?, Teacher_Experience = ?, Teacher_Salary = ? WHERE Teacher_Name = ?"
        sql_query_update_values = (self.age, self.qualification, self.experience, self.salary, self.name)
        mycursor.execute(sql_query_update, sql_query_update_values)
        db_connection.commit()
        return "Success: Updated teacher {} record in our database".format(self.name)


if __name__ == "__main__":
    instance = RetrieveTeacherInfo()

