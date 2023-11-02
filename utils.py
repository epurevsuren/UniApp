import re

# Constants
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@university\.com$"
PASS_REGEX = r"^[A-Z].{5,}[0-9]{3,}$"


class Utils:
    @staticmethod
    def is_valid_email(email):
        return re.match(EMAIL_REGEX, email)

    @staticmethod
    def is_valid_password(password):
        return re.match(PASS_REGEX, password)
