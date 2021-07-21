import os
import numpy as np

from module.deformers.ARAPDeformer import ARAPDeformer
from pipeline.Pipeline import Pipeline

curr_dir = os.path.dirname(os.path.realpath(__file__))
data_in_dir = "data_in"
data_out_dir = "data_out"
file_name = "head.obj"

in_path = os.path.join(curr_dir, data_in_dir, file_name)
out_path = os.path.join(curr_dir, data_out_dir, "arap_head_test.obj")


p = Pipeline(1)
c = {}
for k, f in ARAPDeformer.get_applicable_configs().items():
    q = np.random.uniform()
    c[k] = f(q)
d = ARAPDeformer(c)
p.plug(d)

p.process_shape_file(in_path, out_path)
