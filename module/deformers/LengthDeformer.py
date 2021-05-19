from copy import deepcopy
from typing import Dict, Callable, Tuple

import numpy as np

from module.Deformer import Deformer


X = "x"
Y = "y"
Z = "z"


class LengthDeformer(Deformer):
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        nv = deepcopy(v)
        nf = deepcopy(f)
        for i, (c, m) in enumerate(self.config.items()):
            nv[:, i] *= m
        return nv, nf

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        sampler = lambda q: 2 ** (q * 2 - 1)
        return {X: sampler, Y: sampler, Z: sampler}
