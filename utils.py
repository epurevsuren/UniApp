import re

# Constants
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]{6,}+@university\.com$"
PASSWORD_REGEX = r"^(?=.*[A-Z])(?=.*\d).{6,}$"


class Utils:
    @staticmethod
    def is_valid_email(email):
        return re.match(EMAIL_REGEX, email)

    @staticmethod
    def is_valid_password(password):
        return re.match(PASSWORD_REGEX, password)
