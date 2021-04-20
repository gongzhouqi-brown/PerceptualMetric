from copy import deepcopy
from typing import Dict, Callable, Tuple

import igl
import numpy as np

from module.Deformer import Deformer


PIVOTS = "pivots"
FIRST = "first"
SECOND = "second"
THIRD = "third"
FOURTH = "fourth"
PIVOT_LABEL = [FIRST, SECOND, THIRD, FOURTH]


class BiharmonicDeformer(Deformer):
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

        x_len = (max_x - min_x) * 0.5
        y_len = (max_y - min_y) * 0.5
        z_len = (max_z - min_z) * 0.5

        x_mid = x_len + min_x
        y_mid = y_len + min_y
        z_mid = z_len + min_z

        largest_len = max(x_len, y_len, z_len)

        center = np.array([x_mid, y_mid, z_mid])

        # 0 fix, 1 move, -1 flow
        s = []

        deform_centers = []
        for i in range(int(self.config[PIVOTS])):
            deform_centers.append(v[int(np.floor(self.config[PIVOT_LABEL[i]] * len(v)))])
        for ve in v:
            dist = min([np.linalg.norm(ve - dc) for dc in deform_centers])
            if dist < 0.05 * largest_len:
                s.append(1)
            elif dist < 0.5 * largest_len:
                s.append(-1)
            else:
                s.append(0)
        s = np.array(s)

        b = np.array([[t[0] for t in [(i, s[i]) for i in range(0, v.shape[0])] if t[1] >= 0]]).T
        b = b.astype(f.dtype)

        u_bc = np.zeros((b.shape[0], v.shape[1]))
        v_bc = np.zeros((b.shape[0], v.shape[1]))

        for bi in range(b.shape[0]):
            v_bc[bi] = v[b[bi]]

            if s[b[bi]] == 0:  # Don't move handle 0
                u_bc[bi] = v[b[bi]]
            elif s[b[bi]] == 1:
                old = v[b[bi]]
                displacement = old - center
                displacement *= 1.6
                u_bc[bi] = center + displacement

        d_bc = u_bc - v_bc
        d = igl.harmonic_weights(v, f, b, d_bc, 2)
        u = v + d
        return u, deepcopy(f)

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        num_pivos_sampler = lambda q: np.floor(q * 4 + 1)
        random_point_sampler = lambda q: q
        cfg = {PIVOTS: num_pivos_sampler}
        for lbl in PIVOT_LABEL:
            cfg[lbl] = random_point_sampler
        return cfg
