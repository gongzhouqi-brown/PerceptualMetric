import os

from data.ShapeNet import random_shape_net_object
from pipeline.Pipeline import Pipeline
from module.deformers.MarchingCubesDeformer import MarchingCubesDeformer

curr_dir = os.path.dirname(os.path.realpath(__file__))
data_in_dir = "data_in"
data_out_dir = "data_out"
file_name = "head.obj"


def shape_net_test():
    for i in range(10):
        in_path = random_shape_net_object()

        print(in_path)

        out_path = os.path.join(curr_dir, data_out_dir, "mc{}.obj".format(i))

        p = Pipeline(1)
        d = MarchingCubesDeformer({})
        p.plug(d)

        p.process_shape_file(in_path, out_path)


def head_test():
    in_path = os.path.join(curr_dir, data_in_dir, file_name)
    out_path = os.path.join(curr_dir, data_out_dir, "marching_cubes_head_test.obj")

    p = Pipeline(1)
    d = MarchingCubesDeformer({})
    p.plug(d)

    p.process_shape_file(in_path, out_path)

head_test()