import re

# Constants
EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"
PASSWORD_REGEX = r"^(?=.*[A-Z])(?=.*\d).{6,}$"


class Utils:
    @staticmethod
    def is_valid_email(email):
        return re.match(EMAIL_REGEX, email)

    @staticmethod
    def is_valid_password(password):
        return re.match(PASSWORD_REGEX, password)
