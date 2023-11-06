from colors import Colors
from student_controller import StudentController
from subject_controller import SubjectController


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
                            if StudentController.changePassword(student, new_password):
                                print("Password updated successfully.")
                            else:
                                print(Colors.red("Incorrect password format"))
                            break
                        else:
                            print(Colors.red("Password does not match - try again"))
                elif choice == "e":
                    subject = SubjectController.createSubject()
                    if SubjectController.checkLimit(student):
                        print(Colors.yellow(f"Enrolling in Subject-{subject.id}"))
                        SubjectController.enrollSubject(student, subject)
                        print(
                            Colors.yellow(
                                f"You are now enrolled in {len(student.subjects)} out of 4 subjects"
                            )
                        )
                    else:
                        print(
                            Colors.red(
                                "Students are allowed to enrol in 4 subjects only"
                            )
                        )
                elif choice == "r":
                    subject_id = input("Remove Subject by ID: ")
                    print(Colors.yellow(f"Dropping Subject-{subject_id}"))
                    if SubjectController.removeSubject(student, subject_id):
                        print(
                            Colors.yellow(
                                f"You are now enrolled in {len(student.subjects)} out of 4 subjects"
                            )
                        )
                    else:
                        print(
                            Colors.red(
                                f"Subject {subject_id} not found in enrolled subjects"
                            )
                        )
                elif choice == "s":
                    print(Colors.yellow(f"Showing {len(student.subjects)} subjects"))
                    for subject in student.subjects:
                        print(
                            f"[ Subject::{subject.id} -- mark = {subject.mark} -- grade = {subject.grade: >4} ]"  # Filling spaces 4 times
                        )
                elif choice == "x":
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
