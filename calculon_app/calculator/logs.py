import logging
from colorama import init, Fore, Style 

# Уровень логирования
logging.basicConfig(level=logging.INFO)
# Инициализируем coloram-у
init(autoreset=True)


class LogClass:


    def __init__(self):
        pass


    def info_message(self, mesg):
        """
        Log info message 
        """
        logging.info(
            f'{Fore.YELLOW}[info]{mesg}{Style.RESET_ALL}'
        )
