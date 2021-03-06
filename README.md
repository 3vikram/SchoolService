# SchoolService
This service helps to manage the teachers and students records via REST API services

REST Services created can be used by downloading the POSTMan dump from https://www.getpostman.com/collections/51f216cda1a1e3e8ee57

1. POST requests (requires API secret in the HTTP request),

    Create Student information via /student/create
  
    Create Teacher information via /teacher/create
  
    Register users to manage School DB information via /user/register (No API secret required)
  
    Login users via /user/login
  
2. PUT requests (requires API secret in the HTTP request),

    Update Student information via /student/update
    
    Update Teacher information via /teacher/update

3. GET requests (requires API secret in the HTTP request for getting teachers and students information),

    Get teachers information by passing teacher's ID in the URL, /teacher/teacherId/<Teacher_ID>
    
    Get students information by passing student's ID in the URL, /student/studentId/<Student_ID>
  
    Get number of teachers in the school via /teacher/count
  
    Get number of students in the school via /student/count
  
    Logout users via /user/logout
  
4. DEL requests (requires API secret in the HTTP request),

    Delete teacher record via /teacher/remove
  
    Delete student record via /student/remove
