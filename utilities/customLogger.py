import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Training\\nopcommerceApp\\Logs\\automation.log",
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
