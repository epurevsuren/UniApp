from student_course_system import StudentCourseSystem
from student_controller import StudentController
from colors import Colors


class StudentSystem:
    @staticmethod
    def run():
        while True:
            try:
                print(
                    Colors.bright_cyan("Student System (l/r/x): "),
                    end="",
                )
                choice = input().strip().lower()
                if choice == "l":
                    StudentSystem.login_student()
                elif choice == "r":
                    StudentSystem.register_student()
                elif choice == "x":
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

    @staticmethod
    def login_student():
        print(Colors.bright_green("Student Sign In"))
        while True:
            email = input("Email: ")
            password = input("Password: ")

            if StudentController.checkFormat(email, password):
                print(Colors.yellow("email and password formats acceptable"))
            else:
                print(Colors.red("Incorrect email or password format"))
                continue

            student = StudentController.checkExist(email)
            if student is None:
                print(Colors.red("Student does not exist"))
                break

            if StudentController.login(email, password) is not None:
                StudentCourseSystem.run(student)
                break
            else:
                print(Colors.red("Incorrect password"))

    @staticmethod
    def register_student():
        print(Colors.bright_green("Student Sign Up"))
        while True:
            try:
                email = input("Email: ")
                password = input("Password: ")

                if StudentController.checkFormat(email, password):
                    print(Colors.yellow("email and password formats acceptable"))
                else:
                    print(Colors.red("Incorrect email or password format"))
                    continue

                student = StudentController.checkExist(email)
                if student is not None:
                    print(Colors.red(f"Student {student.name} already exists"))
                    continue

                name = input("Name: ")
                StudentController.addStudent(name, email, password)
                print(Colors.yellow(f"Enrolling Student {name}"))
                break
            except Exception as e:
                print(f"An error occurred: {e}")
