from api.main import api
from loader import config

import uvicorn, handlers

from misc.logs import initialize_logging

if __name__ == '__main__':
    initialize_logging(path = config.logging.path)
    uvicorn.run(api, host = config.api.host, port = config.api.port)