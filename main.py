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
from pipeline.Pipeline import run_random_pipeline


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


def random_shape_sample():
    t = [r"/home/zgong8/new_SN/02992529/a3bc032d0842d570348e2c62a688b780/models/model_normalized.obj",
         r"/home/zgong8/new_SN/02992529/6d053ef40bedd8fcbfa0195eb6461a44/models/model_normalized.obj",
         r"/home/zgong8/new_SN/02992529/c43c9123ed893de5a0eb5a85db887292/models/model_normalized.obj",
         r"/home/zgong8/new_SN/02992529/2df0bc8b46ad3cb858932236a22029d3/models/model_normalized.obj",
         r"/home/zgong8/new_SN/02992529/ab3ebae8a44e1ae8ca47cd18decbac61/models/model_normalized.obj",
         r"/home/zgong8/new_SN/02992529/976a8d10e8423f8d8f15e8aad14ff29e/models/model_normalized.obj",
         r"/home/zgong8/new_SN/02992529/2dccc7cfff6f9a28aca331f9e5d9fa9/models/model_normalized.obj",
         r"/home/zgong8/new_SN/02992529/b442b550e827cbcc8ea897fbf75dc392/models/model_normalized.obj",
         r"/home/zgong8/new_SN/02992529/500fbdefb58e261af2cdad303f49c9f9/models/model_normalized.obj"]
    for i, in_path in enumerate(t):
        out_path = r"/home/zgong8/PerceptualMetric/sample_out/" + str(i) + ".obj"
        file_path = r"/home/zgong8/PerceptualMetric/sample_out/" + str(i) + ".txt"
        ppl, status = run_random_pipeline(in_path, out_path)
        with open(file_path, 'w') as f:
            f.write(str(ppl))
            f.write("\n")
            f.write(str(status))
        f.close()


if __name__ == '__main__':
    initialize()
    random_shape_sample()
    # p = get_object("04379243", "eb773e1b74c883a070d809fda3b93e7b")
    # manifold_object(p, r"/home/zgong8/outputs/simplified_out.obj")


