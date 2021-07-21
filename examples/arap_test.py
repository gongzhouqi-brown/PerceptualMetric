import os
import numpy as np

from data.ShapeNet import random_shape_net_object
from module.deformers.ARAPDeformer import ARAPDeformer
from pipeline.Pipeline import Pipeline

curr_dir = os.path.dirname(os.path.realpath(__file__))
data_in_dir = "data_in"
data_out_dir = "data_out"
file_name = "head.obj"

in_path = os.path.join(curr_dir, data_in_dir, file_name)
out_path = os.path.join(curr_dir, data_out_dir, "rc_head_test.obj")


def test():
    in_path = os.path.join(curr_dir, data_out_dir, "mc5b_decimation.obj")
    out_path = os.path.join(curr_dir, data_out_dir, "mc5b_arap.obj")

    p = Pipeline(1)
    c = {}
    for k, f in ARAPDeformer.get_applicable_configs().items():
        q = np.random.uniform()
        c[k] = f(q)
    d = ARAPDeformer(c)
    p.plug(d)

    p.process_shape_file(in_path, out_path)






def shape_net_test():
    for i in range(10):
        in_path = random_shape_net_object()

        print(in_path)

        out_path = os.path.join(curr_dir, data_out_dir, "arap{}.obj".format(i))

        p = Pipeline(1)
        c = {}
        for k, f in ARAPDeformer.get_applicable_configs().items():
            q = np.random.uniform()
            c[k] = f(q)
        d = ARAPDeformer(c)
        p.plug(d)

        p.process_shape_file(in_path, out_path)

if __name__ == '__main__':
    shape_net_test()
