import os
import pickle


class Database:
    FILENAME = "students.data"

    @staticmethod
    def check_file_existence():
        return os.path.exists(Database.FILENAME)

    @staticmethod
    def create_file_if_not_exists():
        if not Database.check_file_existence():
            with open(Database.FILENAME, "wb") as file:
                pickle.dump([], file)

    @staticmethod
    def write_students_to_file(students):
        with open(Database.FILENAME, "wb") as file:
            pickle.dump(students, file)

    @staticmethod
    def read_students_from_file():
        if Database.check_file_existence():
            with open(Database.FILENAME, "rb") as file:
                students = pickle.load(file)
                return students
        else:
            return []

    @staticmethod
    def clear_file():
        if Database.check_file_existence():
            os.remove(Database.FILENAME)
            Database.create_file_if_not_exists()

    @staticmethod
    def find_student_by_email(email):
        students = Database.read_students_from_file()
        for student in students:
            if student.email == email:
                return student
        return None

    @staticmethod
    def find_student_by_id(student_id):
        students = Database.read_students_from_file()
        for student in students:
            if student.id == student_id:
                return student
        return None

    @staticmethod
    def add_student(student):
        students = Database.read_students_from_file()
        students.append(student)
        Database.write_students_to_file(students)

    @staticmethod
    def remove_student(student):
        students = Database.read_students_from_file()
        for i, s in enumerate(students):
            if s.id == student.id:
                students.remove(s)
                break
        else:
            students.remove(student)
        Database.write_students_to_file(students)

    @staticmethod
    def update_student(student):
        students = Database.read_students_from_file()
        for i, s in enumerate(students):
            if s.id == student.id:
                students[i] = student
                break
        else:
            students.append(student)
        Database.write_students_to_file(students)

    @staticmethod
    def match(email, password):
        students = Database.read_students_from_file()
        for student in students:
            if student.email == email and student.password == password:
                return student
        return None
