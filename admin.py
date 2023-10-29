from database import Database
from colors import Colors


class Admin:
    @staticmethod
    def run():
        while True:
            try:
                print(
                    Colors.bright_cyan("Admin System (c/g/p/r/s/x): "),
                    end="",
                )
                choice = input().strip().lower()
                if choice == "c":
                    print(Colors.yellow("Clearing students database"))
                    confirmation = (
                        input(
                            Colors.red(
                                "Are you sure you want to clear the database (Y)ES/(N)O: "
                            )
                        )
                        .strip()
                        .lower()
                    )
                    if confirmation == "y":
                        Database.clear_file()
                        print(Colors.yellow("Students data cleared"))
                    else:
                        print("Operation canceled.")
                elif choice == "g":
                    Admin.group_students()
                elif choice == "p":
                    Admin.partition_students()
                elif choice == "r":
                    student_id = input("Remove by ID: ")
                    student = Database.find_student_by_id(student_id)
                    if student:
                        Database.remove_student(student)
                        print(Colors.yellow(f"Removing Student {student_id} Account"))
                    else:
                        print(Colors.red(f"Student {student_id} does not exist"))
                elif choice == "s":
                    Admin.show_students()
                elif choice == "x":
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

    @staticmethod
    def group_students():
        students = Database.read_students_from_file()
        if students:
            print(Colors.yellow("Grade Grouping"))
            grades = {}
            for student in students:
                avg_mark = student.calculate_average_mark()
                grade = student.calculate_grade()
                if grade not in grades:
                    grades[grade] = []
                grades[grade].append(
                    f"{student.name} :: {student.id} --> GRADE: {grade} - MARK: {avg_mark:.2f}"
                )

            for grade, students in grades.items():
                print(f"{grade}  ", end="")
                for student_info in students:
                    print("--> [" + student_info + "]")
        else:
            print("     < Nothing to display >")

    @staticmethod
    def partition_students():
        students = Database.read_students_from_file()
        if students:
            print(Colors.yellow("PASS/ FAIL Partition"))
            pass_students = []
            fail_students = []
            for student in students:
                if student.calculate_grade() == "Z":
                    fail_students.append(student)
                else:
                    pass_students.append(student)

            print("PASS --> [", end="")
            for idx, student in enumerate(pass_students):
                print(
                    f"{student.name} :: {student.id} --> GRADE: {student.calculate_grade()} - MARK: {student.calculate_average_mark():.2f}",
                    end="",
                )
                if idx != len(pass_students) - 1:
                    print(", ", end="")
            print("]")

            print("FAIL --> [", end="")
            for idx, student in enumerate(fail_students):
                print(
                    f"{student.name} :: {student.id} --> GRADE: Z - MARK: {student.calculate_average_mark():.2f}",
                    end="",
                )
                if idx != len(fail_students) - 1:
                    print(", ", end="")

            print("]")
        else:
            print("     < Nothing to display >")

    @staticmethod
    def show_students():
        print(Colors.yellow("Student List"))
        students = Database.read_students_from_file()
        if students:
            for student in students:
                print(f"{student.name} :: {student.id} --> Email: {student.email}")
        else:
            print("     < Nothing to display >")
