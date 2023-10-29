import random


class Subject:
    def __init__(self, subject_id=None):
        self.id = subject_id if subject_id is not None else self.generate_subject_id()
        self.mark = random.randint(25, 100)
        self.grade = self.calculate_grade()

    def generate_subject_id(self):
        return str(random.randint(1, 999)).zfill(3)

    def calculate_grade(self):
        mark = self.mark
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
