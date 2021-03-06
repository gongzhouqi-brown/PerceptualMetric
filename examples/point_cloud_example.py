import os

from pipeline.Pipeline import Pipeline
from module.deformers.PointCloudDeformer import PointCloudDeformer

curr_dir = os.path.dirname(os.path.realpath(__file__))
data_in_dir = "data_in"
data_out_dir = "data_out"
file_name = "head.obj"

in_path = os.path.join(curr_dir, data_in_dir, file_name)
out_path = os.path.join(curr_dir, data_out_dir, "pcd_head_test.obj")

p = Pipeline(1)
d = PointCloudDeformer({})
p.plug(d)

p.process_shape_file(in_path, out_path)
