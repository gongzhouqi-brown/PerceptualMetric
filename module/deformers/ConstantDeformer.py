from copy import deepcopy

from module.Deformer import Deformer

import numpy as np


class ConstantDeformer(Deformer):
    def __init__(self, c):
        super().__init__(c)
        self.foo = 1

    def transform(self, v: np.ndarray, f: np.ndarray):
        return deepcopy(v), deepcopy(f)

    @staticmethod
    def get_applicable_configs():
        point_sampler = lambda q: q
        size_sampler = lambda a: a * 10 + 10
        return {"point": point_sampler, "size": size_sampler}

    def pretty(self):
        print(self.config)
        print(type(self.transform))
