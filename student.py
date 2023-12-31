import random


class Student:
    def __init__(self, name, email, password):
        self.id = self.generate_student_id()
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

    def generate_student_id(self):
        return str(random.randint(1, 999999)).zfill(6)

    def change_password(self, new_password):
        self.password = new_password

    def enroll_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject_id):
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                return True
        else:
            return False

    def calculate_average_mark(self):
        total_marks = sum(subject.mark for subject in self.subjects)
        return total_marks / len(self.subjects) if len(self.subjects) > 0 else 0

    def calculate_grade(self):
        mark = self.calculate_average_mark()
        return (
            "HD"
            if mark >= 85
            else "D"
            if mark >= 75
            else "C"
            if mark >= 65
            else "P"
            if mark >= 50
            else "Z"
        )
