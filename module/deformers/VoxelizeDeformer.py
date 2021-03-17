from typing import Dict, Callable, Tuple

import numpy as np
import trimesh
import trimesh.voxel.creation

from module.Deformer import Deformer


NUM_CUBES = "cubes"


class VoxelizeDeformer(Deformer):
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        xs = v[:, 0]
        ys = v[:, 1]
        zs = v[:, 2]
        min_x = min(xs)
        max_x = max(xs)
        min_y = min(ys)
        max_y = max(ys)
        min_z = min(zs)
        max_z = max(zs)

        x_len = max_x - min_x
        y_len = max_y - min_y
        z_len = max_z - min_z

        largest_len = max(x_len, y_len, z_len)

        size = largest_len / self.config[NUM_CUBES]

        mesh = trimesh.Trimesh(v, f, process=False)
        g = trimesh.voxel.creation.voxelize(mesh, size)
        new_mesh = g.as_boxes()
        return np.array(new_mesh.vertices), np.array(new_mesh.faces)

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        sampler = lambda q: 2 ** np.floor(q * 3 + 5)
        return {NUM_CUBES: sampler}
