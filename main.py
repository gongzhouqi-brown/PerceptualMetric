import argparse

from log.logger import setup_logger


def initialize():
    parser = argparse.ArgumentParser(description="Perceptual Metric")
    parser.add_argument("-f", "--filelog",
                        help="Output all logs to a daily log file instead of console.",
                        action="store_true")
    # parser.add_argument("-d", "--data",
    #                     help="Data file specified for running.",
    #                     nargs=1)
    args = vars(parser.parse_args())
    setup_logger(args["filelog"])


if __name__ == '__main__':
    initialize()
