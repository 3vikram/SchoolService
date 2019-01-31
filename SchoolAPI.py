from flask import Flask
from flask import jsonify
from flask import request
from Teachers import *
from Students import *

app = Flask(__name__)

@app.route('/teacherId/<int:userid>', methods=['GET'])
def get_teacher_data(userid):
    teacher_instance = RetrieveTeacherInfo()
    return jsonify(teacher_instance.get_teacher_info(userid))

@app.route('/studentId/<int:studentid>', methods=['GET'])
def get_student_data(studentid):
    instance1 = RetrieveStudentInfo()
    return jsonify(instance1.get_student_info(studentid))

if __name__ == "__main__":
    app.run(debug=True)
