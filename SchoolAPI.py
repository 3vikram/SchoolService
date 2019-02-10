from flask import Flask, make_response
from flask import jsonify
from flask import request
from Teachers import *
from Students import *
from RequestValidation import *

app = Flask(__name__)

@app.route('/teacher/teacherId/<int:userid>', methods=['GET'])
def get_teacher_data(userid):
    headers = request.headers
    auth = headers.get("API-Secret")
    teacher_instance = RetrieveTeacherInfo()
    api_token_validation = RequestValidator()
    if api_token_validation.api_token_validation(auth):
        return jsonify(teacher_instance.get_teacher_info(userid)), {'X-Frame'}
    else:
        return jsonify({"message": "Unauthorised access"}), 403

@app.route('/student/studentId/<int:studentid>', methods=['GET'])
def get_student_data(studentid):
    headers = request.headers
    auth = headers.get("API-Secret")
    student_instance = RetrieveStudentInfo()
    api_token_validation = RequestValidator()
    if api_token_validation.api_token_validation(auth):
        return jsonify(student_instance.get_student_info(studentid))
    else:
        return jsonify({"message": "Unauthorised access"}), 403

@app.route('/student/create', methods=['POST'])
def create_student():
    headers = request.headers
    auth = headers.get("API-Secret")
    data = request.get_json()
    student_name = data['sname']
    student_age = data['sage']
    student_class = data['sclass']
    student_section = data['ssection']
    create_student_info = RetrieveStudentInfo()
    api_token_validation = RequestValidator()
    if api_token_validation.api_token_validation(auth):
        return jsonify(create_student_info.set_student_info(student_name, student_age, student_class, student_section))
    else:
        return jsonify({"message": "Unauthorised access"}), 403

@app.route('/teacher/create', methods=['POST'])
def create_teacher():
    headers = request.headers
    auth = headers.get("API-Secret")
    data = request.get_json()
    teacher_name = data['tname']
    teacher_age = data['tage']
    teacher_qualification = data['tqualification']
    teacher_experience = data['texperience']
    teacher_salary = data['tsalary']
    create_teacher_info = RetrieveTeacherInfo()
    api_token_validation = RequestValidator()
    if api_token_validation.api_token_validation(auth):
        return jsonify(create_teacher_info.set_teacher_info(teacher_name, teacher_age, teacher_qualification, teacher_experience, teacher_salary))
    else:
        return jsonify({"message": "Unauthorised access"}), 403

@app.route('/teacher/count', methods=['GET'])
def total_teachers():
    total_teachers_instance = RetrieveTeacherInfo()
    response= make_response(jsonify(total_teachers_instance.get_total_teachers()))
    response.headers["X-FRAME-OPTIONS"] = "DENY"
    return response

@app.route('/student/count', methods=['GET'])
def total_students():
    total_students_instance = RetrieveStudentInfo()
    return jsonify(total_students_instance.get_total_students())

@app.route('/teacher/remove', methods=['DELETE'])
def delete_teacher():
    headers = request.headers
    auth = headers.get("API-Secret")
    data = request.get_json()
    teacher_ID = data['tid']
    create_teacher_remove = RetrieveTeacherInfo()
    api_token_validation = RequestValidator()
    if api_token_validation.api_token_validation(auth):
        return jsonify(create_teacher_remove.remove_teacher(teacher_ID))
    else:
        return jsonify({"message": "Unauthorised access"}), 403

@app.route('/student/remove', methods=['DELETE'])
def delete_student():
    headers = request.headers
    auth = headers.get("API-Secret")
    data = request.get_json()
    student_ID = data['sid']
    create_student_remove = RetrieveStudentInfo()
    api_token_validation = RequestValidator()
    if api_token_validation.api_token_validation(auth):
        return jsonify(create_student_remove.remove_student(student_ID))
    else:
        return jsonify({"message": "Unauthorised access"}), 403

@app.route('/teacher/update', methods=['PUT'])
def update_teacher():
    headers = request.headers
    auth = headers.get("API-Secret")
    data = request.get_json()
    teacher_name = data['tname']
    teacher_age = data['tage']
    teacher_qualification = data['tqualification']
    teacher_experience = data['texperience']
    teacher_salary = data['tsalary']
    create_teacher_info = RetrieveTeacherInfo()
    api_token_validation = RequestValidator()
    if api_token_validation.api_token_validation(auth):
        return jsonify(create_teacher_info.update_teacher_info(teacher_name, teacher_age, teacher_qualification, teacher_experience, teacher_salary))
    else:
        return jsonify({"message": "Unauthorised access"}), 403

@app.route('/student/update', methods=['PUT'])
def update_student():
    headers = request.headers
    auth = headers.get("API-Secret")
    data = request.get_json()
    student_name = data['sname']
    student_age = data['sage']
    student_class = data['sclass']
    student_section = data['ssection']
    create_student_info = RetrieveStudentInfo()
    api_token_validation = RequestValidator()
    if api_token_validation.api_token_validation(auth):
        return jsonify(create_student_info.update_student_info(student_name, student_age, student_class, student_section))
    else:
        return jsonify({"message": "Unauthorised access"}), 403


if __name__ == "__main__":
    app.run(debug=True)
