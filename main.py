import argparse
import subprocess

from data.ShapeNet import iterate_shape_net, get_object, random_shape_net_object
from examples.random_cage_test import shape_net_test
from examples.validator_example import validate_for_examples
from examples.biharmonic_example import test
from log.logger import setup_logger
from module.Refiner import count_shape_net_components, manifold_object
import os
import igl
import numpy as np
from constant.constant import pivot_path
from module.validator.Validator import is_manifold
from pipeline.Pipeline import run_random_pipeline, Pipeline


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
    for i in range(100):
        in_path = random_shape_net_object()
        out_path_ori = r"/home/zgong8/PerceptualMetric/sample_out/" + str(i) + "-ori.obj"
        out_path1 = r"/home/zgong8/PerceptualMetric/sample_out/" + str(i) + "-1.obj"
        file_path1 = r"/home/zgong8/PerceptualMetric/sample_out/" + str(i) + "-1.txt"
        out_path2 = r"/home/zgong8/PerceptualMetric/sample_out/" + str(i) + "-2.obj"
        file_path2 = r"/home/zgong8/PerceptualMetric/sample_out/" + str(i) + "-2.txt"
        empty_pipeline = Pipeline(0)
        empty_pipeline.process_shape_file(in_path, out_path_ori)
        ppl, status = run_random_pipeline(in_path, out_path1)
        with open(file_path1, 'w') as f:
            f.write(in_path)
            f.write("\n")
            f.write(str(ppl))
            f.write("\n")
            f.write("status: ")
            f.write(str(status))
            if status:
                f.write("\n")
                f.write("manifold: ")
                f.write(str(is_manifold(file=out_path1)))
        f.close()
        ppl, status = run_random_pipeline(in_path, out_path2)
        with open(file_path2, 'w') as f:
            f.write(in_path)
            f.write("\n")
            f.write(str(ppl))
            f.write("\n")
            f.write("status: ")
            f.write(str(status))
            if status:
                f.write("\n")
                f.write("manifold: ")
                f.write(str(is_manifold(file=out_path2)))
        f.close()
        print("{} done!".format(str(i)))


if __name__ == '__main__':
    initialize()
    validate_for_examples()
    #test()
    #shape_net_test()
    # p = get_object("04379243", "eb773e1b74c883a070d809fda3b93e7b")
    # manifold_object(p, r"/home/zgong8/outputs/simplified_out.obj")


