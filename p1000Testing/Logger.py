import inspect
import logging


class Logger:
    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__ + inspect.currentframe().f_back.f_code.co_name)
        file_handler = logging.FileHandler("Log.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def get_logger2():
        log_format = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename="Log.log", level=logging.INFO, format=log_format, filemode="w")
        return logging.getLogger()
