from loader import executor, config
import handlers

from misc.logs import initialize_logging

if __name__ == '__main__':
    initialize_logging(path = config.logging.path)
    executor.start_polling()