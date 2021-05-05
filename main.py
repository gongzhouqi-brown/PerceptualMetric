import argparse

from data.ShapeNet import iterate_shape_net
from log.logger import setup_logger
from module.Refiner import count_shape_net_components
import os
import igl
import numpy as np


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


def size_shape_net():
    old_size = []
    new_size = []
    counter = 0
    for old_path in iterate_shape_net():
        new_path = old_path.replace("ShapeNetCore.v2", "new_SN")
        old_size.append(os.path.getsize(old_path))
        new_size.append(os.path.getsize(new_path))
        counter += 1
        print(counter)
    old_size = np.array(old_size)
    new_size = np.array(new_size)
    np.save("old", old_size)
    np.save("new", new_size)


if __name__ == '__main__':
    initialize()
    size_shape_net()


