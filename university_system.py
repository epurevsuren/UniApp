from admin import Admin
from student_system import StudentSystem
from colors import Colors


class UniversitySystem:
    @staticmethod
    def run():
        while True:
            try:
                print(
                    Colors.bright_cyan(
                        "University System: (A)dmin, (S)tudent, or (X): "
                    ),
                    end="",
                )
                choice = input().strip().lower()
                if choice == "a":
                    Admin.run()
                elif choice == "s":
                    StudentSystem.run()
                elif choice == "x":
                    print(Colors.yellow("Thank You"))
                    break
                else:
                    print(Colors.red("Invalid choice. Please try again."))
            except Exception as e:
                print(f"An error occurred: {e}")
