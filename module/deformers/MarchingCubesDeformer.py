import subprocess
from typing import Dict, Callable, Tuple

import igl
import numpy as np
from igl import SIGNED_DISTANCE_TYPE_DEFAULT, SIGNED_DISTANCE_TYPE_PSEUDONORMAL

from module.Deformer import Deformer

# TODO randomness
class MarchingCubesDeformer(Deformer):
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:

        # nv, nf, _, _, _ = igl.offset_surface(v, f, 0, 64, SIGNED_DISTANCE_TYPE_PSEUDONORMAL)

        igl.write_triangle_mesh("/home/zgong8/temp/mc_tmp_in.obj", v, f)
        subprocess.run(["/home/zgong8/libigl/tutorial/build/bin/705_MarchingCubes", "/home/zgong8/temp/mc_tmp_in.obj", "/home/zgong8/temp/mc_tmp_out_1.obj", "/home/zgong8/temp/mc_tmp_out_2.obj"])
        nv, nf = igl.read_triangle_mesh("/home/zgong8/temp/mc_tmp_out_2.obj", np.float64)
        return nv, nf
        # xs = v[:, 0]
        # ys = v[:, 1]
        # zs = v[:, 2]
        # min_x = min(xs)
        # max_x = max(xs)
        # min_y = min(ys)
        # max_y = max(ys)
        # min_z = min(zs)
        # max_z = max(zs)
        #
        # x_len = max_x - min_x
        # y_len = max_y - min_y
        # z_len = max_z - min_z
        #
        # step = 64
        #
        # x_size = x_len / step
        # y_size = y_len / step
        # z_size = z_len / step
        #
        # samples = []
        #
        # for _x in np.arange(min_x+x_size/2, max_x, x_size):
        #     for _y in np.arange(min_y+y_size/2, max_y, y_size):
        #         for _z in np.arange(min_z+z_size/2, max_z, z_size):
        #             samples.append([_x, _y, _z])
        #
        # samples = np.array(samples)
        #
        # field, _, _ = igl.signed_distance(samples, v, f)
        # nv, nf = mcubes.marching_cubes(field, 0)
        # return nv, nf

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        return {}
