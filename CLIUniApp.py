from database import Database
from university_system import UniversitySystem

if __name__ == "__main__":
    Database.create_file_if_not_exists()
    UniversitySystem.run()
