import logging
from datetime import date


def setup_logger(file_mode):
    if file_mode:
        logging.basicConfig(
            filename="logs/log-{}.txt".format(date.today()),
            format="%(asctime)s %(levelname)-8s %(message)s",
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    else:
        logging.basicConfig(
            format="%(asctime)s %(levelname)-8s %(message)s",
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S",
        )
