import logging
from colorama import init, Fore, Style 

# Уровень логирования
logging.basicConfig(level=logging.INFO)
# Инициализируем coloram-у
init(autoreset=True)


class LogClass:


    def __init__(self):
        pass


    def info_message(self, filename: str, method_name: str, message: str) -> None:
        """
        Log info message 
        """
        logging.info(
            f'{Fore.YELLOW}[info][{filename}][{message}]{message}{Style.RESET_ALL}'
        )
