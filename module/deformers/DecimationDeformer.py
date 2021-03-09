from typing import Dict, Callable, Tuple

import igl
import numpy as np

from module.Deformer import Deformer


RATIO = "ratio"


class DecimationDeformer(Deformer):
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        ratio = int(self.config[RATIO])
        _, nv, nf, _, _ = igl.decimate(v, f, len(f)//ratio)
        return nv, nf

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        sampler = lambda q: np.floor(q * 9 + 2)
        return {RATIO: sampler}
