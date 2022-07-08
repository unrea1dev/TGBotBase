import logging, sys

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(filename)s %(levelname)s] %(message)s', datefmt='%y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("log.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

from aiogram import executor
from bot import dispatcher

if __name__ == '__main__':
    executor.start_polling(dispatcher = dispatcher, skip_updates = True)