import os

from data.ShapeNet import random_shape_net_object
from module.deformers.DecimationDeformer import DecimationDeformer
from pipeline.Pipeline import Pipeline

curr_dir = os.path.dirname(os.path.realpath(__file__))
data_in_dir = "data_in"
data_out_dir = "data_out"


def shape_net_test():
    for i in range(100):
        in_path = random_shape_net_object()

        print(in_path)

        out_path = os.path.join(curr_dir, data_out_dir, "decimation_shape_net_test.obj")

        p = Pipeline(1)
        d = DecimationDeformer({"ratio": 5.0})
        p.plug(d)

        p.process_shape_file(in_path, out_path)


if __name__ == '__main__':
    shape_net_test()