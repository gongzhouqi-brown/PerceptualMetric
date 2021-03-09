from typing import Dict, Callable, Tuple

import igl
import numpy as np

from module.Deformer import Deformer


STEPS = "steps"


class SubdivisionDeformer(Deformer):
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        steps = int(self.config[STEPS])
        nv, nf = igl.loop(v, f, steps)
        return nv, nf

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        sampler = lambda q: np.floor(q * 3 + 1)
        return {STEPS: sampler}
