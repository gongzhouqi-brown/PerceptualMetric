from copy import deepcopy
from typing import Dict, Callable, Tuple

import igl
import numpy as np
import trimesh
import math

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
        num_of_vertex = v.shape[0]
        num_of_face = f.shape[0]

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
        random_point_sampler = lambda q: q
        cfg = {}
        cfg[T_X] = random_point_sampler
        cfg[T_Y] = random_point_sampler
        cfg[T_Z] = random_point_sampler
        cfg[THETA] = lambda q : np.arccos(1 - ROTATION_DEG_COS * q)
        cfg[PHI] = lambda q : 2 * np.pi * q
        cfg[PIVOTS] = random_point_sampler
        return cfg