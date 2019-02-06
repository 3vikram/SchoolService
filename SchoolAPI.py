from flask import Flask
from flask import jsonify
from flask import request
from Teachers import *
from Students import *

app = Flask(__name__)

@app.route('/teacher/teacherId/<int:userid>', methods=['GET'])
def get_teacher_data(userid):
    teacher_instance = RetrieveTeacherInfo()
    return jsonify(teacher_instance.get_teacher_info(userid))

@app.route('/student/studentId/<int:studentid>', methods=['GET'])
def get_student_data(studentid):
    student_instance = RetrieveStudentInfo()
    return jsonify(student_instance.get_student_info(studentid))

@app.route('/student/create', methods=['POST'])
def create_student():
    data = request.get_json()
    student_name = data['sname']
    student_age = data['sage']
    student_class = data['sclass']
    student_section = data['ssection']
    create_student_info = RetrieveStudentInfo()
    return jsonify(create_student_info.set_student_info(student_name, student_age, student_class, student_section))

@app.route('/teacher/create', methods=['POST'])
def create_teacher():
    data = request.get_json()
    teacher_name = data['tname']
    teacher_age = data['tage']
    teacher_qualification = data['tqualification']
    teacher_experience = data['texperience']
    teacher_salary = data['tsalary']
    create_teacher_info = RetrieveTeacherInfo()
    return jsonify(create_teacher_info.set_teacher_info(teacher_name, teacher_age, teacher_qualification, teacher_experience, teacher_salary))

@app.route('/teacher/count', methods=['GET'])
def total_teachers():
    total_teachers_instance = RetrieveTeacherInfo()
    return jsonify(total_teachers_instance.get_total_teachers())

@app.route('/student/count', methods=['GET'])
def total_students():
    total_students_instance = RetrieveStudentInfo()
    return jsonify(total_students_instance.get_total_students())

@app.route('/teacher/remove', methods=['DELETE'])
def delete_teacher():
    data = request.get_json()
    teacher_ID = data['tid']
    create_teacher_remove = RetrieveTeacherInfo()
    return jsonify(create_teacher_remove.remove_teacher(teacher_ID))

@app.route('/student/remove', methods=['DELETE'])
def delete_student():
    data = request.get_json()
    student_ID = data['sid']
    create_student_remove = RetrieveStudentInfo()
    return jsonify(create_student_remove.remove_student(student_ID))

@app.route('/teacher/update', methods=['PUT'])
def update_teacher():
    data = request.get_json()
    teacher_name = data['tname']
    teacher_age = data['tage']
    teacher_qualification = data['tqualification']
    teacher_experience = data['texperience']
    teacher_salary = data['tsalary']
    create_teacher_info = RetrieveTeacherInfo()
    return jsonify(create_teacher_info.update_teacher_info(teacher_name, teacher_age, teacher_qualification, teacher_experience, teacher_salary))

@app.route('/student/update', methods=['PUT'])
def update_student():
    data = request.get_json()
    student_name = data['sname']
    student_age = data['sage']
    student_class = data['sclass']
    student_section = data['ssection']
    create_student_info = RetrieveStudentInfo()
    return jsonify(create_student_info.update_student_info(student_name, student_age, student_class, student_section))


if __name__ == "__main__":
    app.run(debug=True)
