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


def refine_shape_net():
    counter = 0
    for old_path in iterate_shape_net():
        size = os.path.getsize(path)
        v, f = igl.read_triangle_mesh(path)
        faces_num = len(f)
        faces.append(faces_num)
        sizes.append(size)
        counter += 1
        print(counter)
    np.save("data", np.array([faces, sizes]))


def manifold_object(in_path, out_path):
    temp_path = r"/home/zgong8/temp/temp.obj"
    v, f = igl.read_triangle_mesh(in_path)
    size = len(f)
    multiplier = size * 5
    subprocess.run(["./manifold", in_path, temp_path], cwd="/home/zgong8/Manifold/build")
    subprocess.run(["./simplify", "-i", temp_path, "-o", out_path, "-m", "-f", str(multiplier)], cwd=r"/home/zgong8/Manifold/build")


if __name__ == '__main__':
    initialize()
    p = get_object("04379243", "eb773e1b74c883a070d809fda3b93e7b")
    manifold_object(p, r"/home/zgong8/outputs/simplified_out.obj")


