from typing import Dict, Callable, Tuple

import numpy as np
import trimesh
import trimesh.voxel.creation

from module.Deformer import Deformer


class VoxelizeDeformer(Deformer):
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        mesh = trimesh.Trimesh(v, f, process=False)
        g = trimesh.voxel.creation.voxelize(mesh, 1)
        new_mesh = g.as_boxes()
        return np.array(new_mesh.vertices), np.array(new_mesh.faces)

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        return {}
