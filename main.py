import argparse
import subprocess

from data.ShapeNet import iterate_shape_net, get_object
from examples.subdivision_example import max_test
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
    pivots = np.load(r"/home/zgong8/pivots.npy")
    counter = 0
    old = []
    new = []
    for i, old_path in enumerate(iterate_shape_net()):
        if i in pivots:
            counter += 1
            new_path = old_path.replace("ShapeNetCore.v2", "new_SN")
            if os.path.exists(new_path):
                old_size = os.path.getsize(old_path)
                old.append(old_size)
                new_size = os.path.getsize(new_path)
                new.append(new_size)
                print(counter)
            else:
                old.append(-1)
                new.append(-1)
                print(counter, "NOT EXIST")
    np.save("compare", np.array([old, new]))


def refine_shape_net():
    pivots = np.load(r"/home/zgong8/pivots.npy")
    counter = 0
    for i, old_path in enumerate(iterate_shape_net()):
        if i in pivots:
            new_path = old_path.replace("ShapeNetCore.v2", "new_SN")
            manifold_object(old_path, new_path)
            counter += 1
            print(counter)


def manifold_object(in_path, out_path):
    temp_path = r"/home/zgong8/temp/temp.obj"
    v, f = igl.read_triangle_mesh(in_path)
    size = len(f)
    multiplier = size * 5
    subprocess.run(["./manifold", in_path, temp_path], cwd="/home/zgong8/Manifold/build")
    subprocess.run(["./simplify", "-i", temp_path, "-o", out_path, "-m", "-f", str(multiplier)], cwd=r"/home/zgong8/Manifold/build")


if __name__ == '__main__':
    initialize()
    size_shape_net()
    # p = get_object("04379243", "eb773e1b74c883a070d809fda3b93e7b")
    # manifold_object(p, r"/home/zgong8/outputs/simplified_out.obj")


