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


def new_shape_net():
    counter = 0
    for old_path in iterate_shape_net():
        new_path = old_path.replace("ShapeNetCore.v2", "new_SN")
        v, f = igl.read_triangle_mesh(old_path, np.float64)
        igl.write_triangle_mesh(new_path, v, f)
        counter += 1
        print(counter)


if __name__ == '__main__':
    initialize()
    new_shape_net()

