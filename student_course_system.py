from subject import Subject
from colors import Colors
from database import Database


class StudentCourseSystem:
    def run(student):
        while True:
            try:
                print(
                    Colors.bright_cyan("Student Course Menu (c/e/r/s/x): "),
                    end="",
                )
                choice = input().strip().lower()
                if choice == "c":
                    print(Colors.yellow("Updating Password"))
                    new_password = input("New Password: ")
                    while True:
                        confirm_password = input("Confirm Password: ")
                        if new_password == confirm_password:
                            student.change_password(new_password)
                            print("Password updated successfully.")
                            Database.update_student(student)  # Update student
                            break
                        else:
                            print(Colors.red("Password does not match - try again"))
                elif choice == "e":
                    if len(student.subjects) < 4:
                        subject = Subject()
                        student.enroll_subject(subject)
                        print(Colors.yellow(f"Enrolling in Subject-{subject.id}"))
                        print(
                            Colors.yellow(
                                f"You are now enrolled in {len(student.subjects)} out of 4 subjects"
                            )
                        )
                        Database.update_student(student)  # Update student
                    else:
                        print(
                            Colors.red(
                                "Students are allowed to enrol in 4 subjects only"
                            )
                        )
                elif choice == "r":
                    subject_id = input("Remove Subject by ID: ")
                    student.remove_subject(subject_id)
                    Database.update_student(student)  # Update student
                elif choice == "s":
                    print(Colors.yellow(f"Showing {len(student.subjects)} subjects"))
                    for subject in student.subjects:
                        print(
                            f"[ Subject::{subject.id} -- mark = {subject.mark} -- grade = {subject.grade: >4} ]"
                        )
                elif choice == "x":
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
