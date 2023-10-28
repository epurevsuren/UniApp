from database import Database
from student import Student
from utils import Utils


class StudentController:
    @staticmethod
    def checkFormat(email, password):
        if Utils.is_valid_email(email) and Utils.is_valid_password(password):
            return True
        else:
            return False

    @staticmethod
    def checkExist(email):
        student = Database.find_student_by_email(email)
        return student

    @staticmethod
    def login(email, password):
        student = Database.match(email, password)
        return student

    @staticmethod
    def addStudent(name, email, password):
        student = Student(name, email, password)
        Database.add_student(student)

    def changePassword(student, newPassword):
        student.change_password(newPassword)
        Database.update_student(student)  # Update student
