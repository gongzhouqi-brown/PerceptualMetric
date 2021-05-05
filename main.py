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
    counter = 0
    faces = []
    sizes = []
    for path in iterate_shape_net():
        size = os.path.getsize(path)
        v, f = igl.read_triangle_mesh(path)
        faces_num = len(f)
        faces.append(faces_num)
        sizes.append(size)
        counter += 1
        print(counter)
    np.save("data", np.array([faces, sizes]))


if __name__ == '__main__':
    initialize()
    size_shape_net()


