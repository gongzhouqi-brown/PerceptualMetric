import argparse
import subprocess

from data.ShapeNet import iterate_shape_net, get_object
from examples.subdivision_example import max_test
from log.logger import setup_logger
from module.Refiner import count_shape_net_components
import os
import igl
import numpy as np
from constant.constant import pivot_path


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


def list_shape_net():
    pivots = np.load(pivot_path)
    counter = 0
    with open('valid_shapes.txt', 'w') as f:
        for i, old_path in enumerate(iterate_shape_net()):
            if i in pivots:
                counter += 1
                new_path = old_path.replace("ShapeNetCore.v2", "new_SN")
                if os.path.exists(new_path):
                    f.write(new_path)
                    f.write('\n')
                    print(counter)
                else:
                    print(counter, "NOT EXIST")


if __name__ == '__main__':
    initialize()
    list_shape_net()
    # p = get_object("04379243", "eb773e1b74c883a070d809fda3b93e7b")
    # manifold_object(p, r"/home/zgong8/outputs/simplified_out.obj")


