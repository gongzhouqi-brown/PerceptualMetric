from copy import deepcopy
from typing import Dict, Callable, Tuple

import igl
import numpy as np
import math

from module.Deformer import Deformer
from module.deformers.DeformerUtil import rMat

T_X = "t_x"
T_Y = "t_y"
T_Z = "t_z"
THETA = "theta"
PHI = "phi"
PIVOTS = "pivots"
ROTATION_DEG_COS = 0.5
MOVE_PORTION = 0.1
FLOW_PORTION = 0.5


class ARAPDeformer(Deformer):
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        vcp = deepcopy(v)
        num_of_vertex = vcp.shape[0]

        maxlen = (vcp.max(axis=0) - vcp.min(axis=0)).max()

        # load config
        theta = self.config[THETA]
        phi = self.config[PHI]
        rotation = rMat(theta, phi)
        translation = np.array([self.config[T_X], self.config[T_Y], self.config[T_Z]]) * maxlen * MOVE_PORTION

        # load pivot
        pivot =  math.floor(num_of_vertex * self.config[PIVOTS])
        pivot = pivot if pivot < num_of_vertex else pivot - 1

        # 1 move, -1 flow, 0 fix
        s = np.zeros(num_of_vertex)
        for idx, p in enumerate(vcp):
            dist = np.linalg.norm(p - vcp[pivot])
            if dist < maxlen * MOVE_PORTION:
                s[idx] = 1
            elif dist < maxlen * FLOW_PORTION:
                s[idx] = -1
            else:
                s[idx] = 0

        b = np.array([[t[0] for t in [(i, s[i]) for i in range(0, vcp.shape[0])] if t[1] >= 0]]).T
        arap = igl.ARAP(vcp, f, 3, b)
        bc = np.zeros((b.size, 3))
        for i in range(b.shape[0]):
            bc[i] = vcp[b[i]]
            if s[b[i]] == 1:
                bc[i] = rotation @ bc[i] + translation
        vn = arap.solve(bc, vcp)
        return vn, deepcopy(f)
        
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