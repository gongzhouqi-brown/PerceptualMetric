from typing import Dict, Callable, Tuple

import numpy as np

from module.Deformer import Deformer
from module.deformers.cageTransform import CageConfig, Random_Cage_Deform

T_X = "t_x"
T_Y = "t_y"
T_Z = "t_z"
THETA = "theta"
PHI = "phi"
PIVOTS = "pivots"
ROTATION_DEG_COS = 0.1


class RandomCageDeformer(Deformer):
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        maxlen = (v.max(axis=0) - v.min(axis=0)).max()
        theta = self.config[THETA]
        phi = self.config[PHI]
        dx = self.config[T_X]
        dy = self.config[T_Y]
        dz = self.config[T_Z]
        seed = self.config[PIVOTS]

        cc = CageConfig(theta, phi, dx, dy, dz, seed, maxlen)
        nv = Random_Cage_Deform(v, f, cc)
        return nv, f

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        cfg = {T_X: lambda q: q,
               T_Y: lambda q: q,
               T_Z: lambda q: q,
               THETA: lambda q: np.arccos(1 - ROTATION_DEG_COS * q),
               PHI: lambda q: 2 * np.pi * q,
               PIVOTS: lambda q: q}
        return cfg
