class Colors:
    OKCYAN = "\033[96m"
    OKYELLOW = "\033[1;33m"
    OKGREEN = "\033[92m"
    WARNING = "\033[0;31m"
    ENDC = "\033[0m"

    @staticmethod
    def bright_cyan(text):
        return Colors.OKCYAN + text + Colors.ENDC

    @staticmethod
    def yellow(text):
        return Colors.OKYELLOW + text + Colors.ENDC

    @staticmethod
    def bright_green(text):
        return Colors.OKGREEN + text + Colors.ENDC

    @staticmethod
    def red(text):
        return Colors.WARNING + text + Colors.ENDC
