import os
import subprocess

from data.ShapeNet import random_shape_net_object
from pipeline.Pipeline import Pipeline
from module.unfinished.MarchingCubesDeformer import MarchingCubesDeformer

curr_dir = os.path.dirname(os.path.realpath(__file__))
data_in_dir = "data_in"
data_out_dir = "data_out"
file_name = "head.obj"


def head_test():
    in_path = os.path.join(curr_dir, data_in_dir, file_name)
    out_path = os.path.join(curr_dir, data_out_dir, "marching_cubes_head_test.obj")

    p = Pipeline(1)
    d = MarchingCubesDeformer({})
    p.plug(d)

    p.process_shape_file(in_path, out_path)


def shape_net_test():
    std_out_path="/home/zgong8/PerceptualMetric/examples/data_out/mc{}{}.obj"
    for i in range(10):
        in_path = random_shape_net_object()

        print(in_path)
        out_path_ori=std_out_path.format(i, "")
        out_path_a=std_out_path.format(i, "a")
        out_path_b=std_out_path.format(i, "b")
        subprocess.run(["cp", in_path, out_path_ori])
        subprocess.run(["/home/zgong8/libigl/tutorial/build/bin/705_MarchingCubes", in_path, out_path_a, out_path_b])



def shape_net_test2():
    std_out_path="/home/zgong8/PerceptualMetric/examples/data_out/mc{}.obj"
    for i in range(10):
        in_path = random_shape_net_object()

        print(in_path)

        out_path = std_out_path.format(i)

        p = Pipeline(1)
        d = MarchingCubesDeformer({})
        p.plug(d)

        p.process_shape_file(in_path, out_path)
        


if __name__ == '__main__':
    shape_net_test()
