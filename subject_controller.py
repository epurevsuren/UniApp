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

    def createSubjectCustomID(id):
        subject = Subject(id)
        return subject

    @staticmethod
    def enrollSubject(student, subject):
        student.enroll_subject(subject)
        Database.update_student(student)  # Update student

    @staticmethod
    def removeSubject(student, subject_id):
        if student.remove_subject(subject_id):
            Database.update_student(student)  # Update student
            return True
        else:
            return False

    @staticmethod
    def enrolledSubjects(student):
        enrolled_subjects = []
        for subject in student.subjects:
            enrolled_subjects.append(f"Subject-{subject.id}")
        return enrolled_subjects

    @staticmethod
    def getAllSubjects():
        all_subjects = []
        for i in range(0, 10):
            subject = SubjectController.createSubject()
            all_subjects.append(f"Subject-{subject.id}")

        return all_subjects
