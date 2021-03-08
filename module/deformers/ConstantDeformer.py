from copy import deepcopy
from typing import Tuple, Callable, Dict

import numpy as np

from module.Deformer import Deformer


class ConstantDeformer(Deformer):
    def __init__(self, c):
        super().__init__(c)
        self.foo = 1

    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        return deepcopy(v), deepcopy(f)

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        point_sampler = lambda q: q
        size_sampler = lambda a: a * 10 + 10
        return {"point": point_sampler, "size": size_sampler}

    def pretty(self):
        print(self.config)
        print(type(self.transform))
