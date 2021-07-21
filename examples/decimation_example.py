import os

from data.ShapeNet import random_shape_net_object
from module.deformers.DecimationDeformer import DecimationDeformer
from module.validator.Validator import is_manifold
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


def test_on_voxel():
    in_path = r"D:\Graduate\Master\Projects\Metric - Danial Ritchie\PerceptualMetric\examples\data_out\my_vox_head_test_32.obj"

    print(is_manifold(file=in_path))

    print("start 1")
    out_path = os.path.join(curr_dir, data_out_dir, "decimation_vox_2.obj")
    p = Pipeline(1)
    d = DecimationDeformer({"ratio": 2.0})
    p.plug(d)
    p.process_shape_file(in_path, out_path)
    print("done 1")

    print("start 2")
    out_path = os.path.join(curr_dir, data_out_dir, "decimation_vox_10.obj")
    p = Pipeline(1)
    d = DecimationDeformer({"ratio": 10.0})
    p.plug(d)
    p.process_shape_file(in_path, out_path)
    print("done 2")


if __name__ == '__main__':
    test_on_voxel()