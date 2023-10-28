from subject import Subject
from database import Database


class SubjectController:
    maxSubject = 4

    @staticmethod
    def checkLimit(student):
        if len(student.subjects) < SubjectController.maxSubject:
            return True
        else:
            return False

    @staticmethod
    def createSubject():
        subject = Subject()
        return subject

    @staticmethod
    def enrollSubject(student, subject):
        student.enroll_subject(subject)
        Database.update_student(student)  # Update student

    def removeSubject(student, subject_id):
        if student.remove_subject(subject_id):
            Database.update_student(student)  # Update student
            return True
        else:
            return False
