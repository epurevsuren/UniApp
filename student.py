from colors import Colors
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
        if len(self.subjects) < 4:
            self.subjects.append(subject)
        else:
            print(Colors.red("Students are allowed to enroll in 4 subjects only"))

    def remove_subject(self, subject_id):
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                print(Colors.yellow(f"Dropping Subject-{subject_id}"))
                print(
                    Colors.yellow(
                        f"You are now enrolled in {len(self.subjects)} out of 4 subjects"
                    )
                )
                break
        else:
            print(Colors.red(f"Subject {subject_id} not found in enrolled subjects"))

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
