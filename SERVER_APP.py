
from logging.handlers import RotatingFileHandler
from REST_API import *


def init_models_dict():
    models = load_models_file(CONFIG.FILE_NAME)
    load_models_to_dict(models)


def init_logger():
    handler = RotatingFileHandler('ItzikSaltLogs.log', maxBytes=10000, backupCount=1)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)



if __name__ == '__main__':
    init_models_dict()
    init_logger()
    app.logger.info("Start Running Server")
    app.run(port=8000, debug=False)
