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
from util.stringToPipeline import string_to_pipelines


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
        out_path_ori = r"/home/zgong8/data_out/" + str(i) + "-ori.obj"
        out_path1 = r"/home/zgong8/data_out/" + str(i) + "-1.obj"
        file_path1 = r"/home/zgong8/data_out/" + str(i) + "-1.txt"
        out_path2 = r"/home/zgong8/data_out/" + str(i) + "-2.obj"
        file_path2 = r"/home/zgong8/data_out/" + str(i) + "-2.txt"
        empty_pipeline = Pipeline(0)
        empty_pipeline.process_shape_file(in_path, out_path_ori)
        status = False
        while not status:
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
        status = False
        while not status:
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


def debug():
    s = r"<class 'MarchingCubesDeformer.MarchingCubesDeformer'> {} <class 'LengthDeformer.LengthDeformer'> {'x': 0.8585584946847424, 'y': 1.2497535030762963, 'z': 1.1194365076434625} <class 'DecimationDeformer.DecimationDeformer'> {'ratio': 8.0} <class 'RandomCageDeformer.RandomCageDeformer'> {'t_x': 0.6238675275926835, 't_y': 0.6803571228735866, 't_z': 0.021039636197039857, 'theta': 0.28097564127558766, 'phi': 0.816326646306728, 'pivots': 0.9467472027843402} <class 'RandomCageDeformer.RandomCageDeformer'> {'t_x': 0.8876853397486949, 't_y': 0.5315935433129064, 't_z': 0.3911888761050619, 'theta': 0.36074874511511146, 'phi': 3.6074052123307347, 'pivots': 0.5945342632947703} <class 'LengthDeformer.LengthDeformer'> {'x': 0.604145944793599, 'y': 1.2216798900694399, 'z': 1.0704989478658395} <class 'RandomCageDeformer.RandomCageDeformer'> {'t_x': 0.36017135075582085, 't_y': 0.3771138116171606, 't_z': 0.016002395066274544, 'theta': 0.26761048770247675, 'phi': 3.0007024102924764, 'pivots': 0.9714222125776031} <class 'ARAPDeformer.ARAPDeformer'> {'t_x': 0.35341306969899844, 't_y': 0.11384102784135575, 't_z': 0.368233517664869, 'theta': 0.853672361463905, 'phi': 2.1633555063379974, 'pivots': 0.14521404805108684} <class 'RandomCageDeformer.RandomCageDeformer'> {'t_x': 0.48387559520116974, 't_y': 0.10430416340681481, 't_z': 0.5366440194061546, 'theta': 0.37208628760245116, 'phi': 6.048740228011427, 'pivots': 0.07114043848393736} <class 'ARAPDeformer.ARAPDeformer'> {'t_x': 0.9559651247353135, 't_y': 0.5490014127877697, 't_z': 0.3268880929352812, 'theta': 0.2172869905165308, 'phi': 1.3520286667669872, 'pivots': 0.42591774920621184}"

    in_f = r"/home/zgong8/ShapeNetCore.v2/04004475/75e53b4107a95368a3c3591ebf6e2911/models/model_normalized.obj"
    out_f = r"/home/zgong8/PerceptualMetric/debug/out{}.obj"
    ps = string_to_pipelines(s)
    for i, p in enumerate(ps):
        p.process_shape_file(in_f, out_f.format(i))
        in_f = out_f.format(i)
        print(i, "done")


if __name__ == '__main__':
    initialize()
    # debug()
    random_shape_sample()
    #test()
    #shape_net_test()


