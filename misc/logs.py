import logging, sys

def initialize_logging(path : str) -> None:
    logging.basicConfig(
        level = logging.INFO,
        format = '[%(asctime)s] [%(filename)s %(levelname)s] %(message)s', datefmt='%y-%m-%d %H:%M:%S',
        handlers = [
            logging.FileHandler(path, encoding = 'UTF-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )