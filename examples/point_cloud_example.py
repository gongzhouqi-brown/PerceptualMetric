import os

from data.ShapeNet import random_shape_net_object
from pipeline.Pipeline import Pipeline
from module.deformers.PointCloudDeformer import PointCloudDeformer

curr_dir = os.path.dirname(os.path.realpath(__file__))
data_in_dir = "data_in"
data_out_dir = "data_out"
file_name = "head.obj"


def head_test():
    in_path = os.path.join(curr_dir, data_in_dir, file_name)
    out_path = os.path.join(curr_dir, data_out_dir, "marching_cubes_head_test.obj")

    p = Pipeline(1)
    d = PointCloudDeformer({})
    p.plug(d)

    p.process_shape_file(in_path, out_path)


def shape_net_test():
    for i in range(10):
        in_path = random_shape_net_object()

        print(in_path)

        out_path = os.path.join(curr_dir, data_out_dir, "pcd{}.obj".format(i))

        p = Pipeline(1)
        d = PointCloudDeformer({})
        p.plug(d)

        p.process_shape_file(in_path, out_path)


if __name__ == '__main__':
    shape_net_test()
    """
    /home/zgong8/ShapeNetCore.v2/04379243/6c0ee01fb43f8f46c045ebb62fca20c6/models/model_normalized.obj
<module.unfinished.PointCloudDeformer.PointCloudDeformer object at 0x7f3621ff2670> done
/home/zgong8/ShapeNetCore.v2/03261776/17c9866b42ae1831df4cfe396cee719e/models/model_normalized.obj
<module.unfinished.PointCloudDeformer.PointCloudDeformer object at 0x7f3647f97dc0> done
/home/zgong8/ShapeNetCore.v2/03642806/5a13f7551c20eb29f3ebfe51dc60263e/models/model_normalized.obj
<module.unfinished.PointCloudDeformer.PointCloudDeformer object at 0x7f3616701bb0> done
/home/zgong8/ShapeNetCore.v2/04225987/f9efb1b00b79c035c1cb365152372fc5/models/model_normalized.obj
<module.unfinished.PointCloudDeformer.PointCloudDeformer object at 0x7f36480274f0> done
/home/zgong8/ShapeNetCore.v2/03636649/d83fc71f3978130e335fe03ac3704320/models/model_normalized.obj
<module.unfinished.PointCloudDeformer.PointCloudDeformer object at 0x7f3621ff2670> done
/home/zgong8/ShapeNetCore.v2/04460130/224934a28705403238cd8eb23853c009/models/model_normalized.obj
<module.unfinished.PointCloudDeformer.PointCloudDeformer object at 0x7f3647f97dc0> done
/home/zgong8/ShapeNetCore.v2/02801938/3e88bbe0b7f7ab5a36b0f2a1430e993a/models/model_normalized.obj
<module.unfinished.PointCloudDeformer.PointCloudDeformer object at 0x7f3621ff2760> done
/home/zgong8/ShapeNetCore.v2/03636649/cfebf5d2a0382ee3fcb8d8c6d4df8143/models/model_normalized.obj
<module.unfinished.PointCloudDeformer.PointCloudDeformer object at 0x7f3647f97be0> done
/home/zgong8/ShapeNetCore.v2/03948459/ca012a47cf5efca23f9d84f9a87a44e4/models/model_normalized.obj
<module.unfinished.PointCloudDeformer.PointCloudDeformer object at 0x7f3647f97dc0> done
/home/zgong8/ShapeNetCore.v2/04004475/db9d02b583bdc8cec25c9cef92ff2800/models/model_normalized.obj
<module.unfinished.PointCloudDeformer.PointCloudDeformer object at 0x7f3648027250> done
    """
