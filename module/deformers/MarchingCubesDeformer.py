from copy import deepcopy
from typing import Dict, Callable, Tuple

import numpy as np

from module.Deformer import Deformer


class MarchingCubesDeformer(Deformer):
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        # TODO: Implement with igl.offset_surface
        # vertices, triangles = mcubes.marching_cubes_func(v, f, 16)
        return deepcopy(v), deepcopy(f)

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        return {}