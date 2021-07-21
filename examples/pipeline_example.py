import log
import os

from data.ShapeNet import random_shape_net_object
from module.deformers.BiharmonicDeformer import BiharmonicDeformer
from module.deformers.DecimationDeformer import DecimationDeformer
from module.deformers.MarchingCubesDeformer import MarchingCubesDeformer
from module.deformers.PointCloudDeformer import PointCloudDeformer
from module.deformers.LengthDeformer import ScaleDeformer
from module.deformers.SubdivisionDeformer import SubdivisionDeformer
from module.deformers.VoxelizeDeformer import VoxelizeDeformer
from pipeline.Pipeline import run_random_pipeline
from pipeline.Pipeline import Pipeline

curr_dir = os.path.dirname(os.path.realpath(__file__))
data_in_dir = "data_in"
data_out_dir = "data_out\\ShapeNet pipeline test"
file_name = "head.obj"


def single_test():
    in_path = os.path.join(curr_dir, data_in_dir, file_name)
    out_path = os.path.join(curr_dir, data_out_dir, "pipeline_head_test.obj")

    run_random_pipeline(in_path, out_path)


def shape_net_test():
    for i in range(100):
        in_path = random_shape_net_object()
        out_path = os.path.join(curr_dir, data_out_dir, "{}.obj".format(i))
        # try:
        print(i, in_path)
        run_random_pipeline(in_path, out_path)
        # except ValueError:
        #     print(in_path)


def reproduce_bug():
    """
    VoxelizeDeformer cannot appear before DecimationDeformer (directly?)
    :return:
    """
    p = Pipeline(2)
    in_path = os.path.join(curr_dir, data_in_dir, file_name)
    out_path = os.path.join(curr_dir, data_out_dir, "bug.obj")
    # p.plug(SubdivisionDeformer({'steps':2.0}))
    # p.plug(DecimationDeformer({'ratio':8.0}))
    p.plug(VoxelizeDeformer({'cubes':128.0}))
    # p.plug(ScaleDeformer({'x':0.84268631133711, 'y':1.7692875780435733, 'z':0.5491969010315603}))
    p.plug(DecimationDeformer({'ratio':5.0}))
    p.process_shape_file(in_path, out_path)


def reproduce_bug2():
    """
    Too large size, crashed. Need a way to prevent this from happening (need order!!!)
    :return:
    """
    p = Pipeline(5)
    in_path = os.path.join(curr_dir, data_in_dir, file_name)
    out_path = os.path.join(curr_dir, data_out_dir, "bug2.obj")
    p.plug(DecimationDeformer({'ratio':8.0}))
    p.plug(DecimationDeformer({'ratio':3.0}))
    p.plug(VoxelizeDeformer({'cubes': 128}))
    p.plug(PointCloudDeformer({}))
    p.plug(SubdivisionDeformer({'steps': 3.0}))
    p.process_shape_file(in_path, out_path)


def reproduce_bug3():
    """
    Decimation?
    :return:
    """
    p = Pipeline(2)
    in_path = "D:\\Graduate\\Master\\Projects\\Metric - Danial Ritchie\\ShapeNetCore.v2\\03636649\\5bb0ad1e0c9432b2dc6493177a28df03\\models\\model_normalized.obj"
    out_path = os.path.join(curr_dir, data_out_dir, "bug3.obj")
    # p.plug(PointCloudDeformer({}))
    p.plug(DecimationDeformer({'ratio': 5.0}))
    p.plug(VoxelizeDeformer({'cubes': 64.0}))
    # p.plug(PointCloudDeformer({}))
    # p.plug(SubdivisionDeformer({'steps': 3.0}))
    # p.plug(BiharmonicDeformer({'pivots': 1.0, 'first': 0.7385002124157157, 'second': 0.2252248122854552, 'third': 0.6892225958888107, 'fourth': 0.8426677800589979}))
    # p.plug(VoxelizeDeformer({'cubes': 128.0}))
    # p.plug(MarchingCubesDeformer({}))
    p.process_shape_file(in_path, out_path)



if __name__ == '__main__':
    # shape_net_test()
    # reproduce_bug3()
    p = Pipeline(0)
    in_path = "D:\\Graduate\\Master\\Projects\\Metric - Danial Ritchie\\ShapeNetCore.v2\\02843684\\4abad12b5ed565da7720fd193c09c4db\\models\\model_normalized.obj"
    out_path = os.path.join(curr_dir, data_out_dir, "bird_house.obj")
    p.process_shape_file(in_path, out_path)