from abc import ABC, abstractmethod
from os import listdir
from os.path import join
from typing import Dict, Tuple, Callable

import importlib.util
import numpy as np
import os


_MODULES_FOLDER = "deformers"
_PYTHON_EXT = ".py"
_DEFORMER_EXT = "Deformer.py"
_SAMPLE_MODULE = "ConstantDeformer"

_ALL_MODULES = None


class Deformer(ABC):
    def __init__(self, config: Dict[str, float]):
        self.config = config

    @abstractmethod
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        pass

    @staticmethod
    @abstractmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        pass


def get_random_deformation() -> Deformer:
    global _ALL_MODULES
    if _ALL_MODULES is None:
        _ALL_MODULES = []
        modules_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), _MODULES_FOLDER)
        modules = [f[:-3] for f in listdir(modules_folder) if f.endswith(_DEFORMER_EXT) and not f.startswith(_SAMPLE_MODULE)]
        for module in modules:
            spec = importlib.util.spec_from_file_location(module, join(modules_folder, module+_PYTHON_EXT))
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            _ALL_MODULES.append(getattr(m, module))
    clazz = np.random.choice(_ALL_MODULES)
    configs = clazz.get_applicable_configs()
    config = {}
    for c, f in configs.items():
        q = np.random.uniform()
        config[c] = f(q)
    return clazz(config)


def name_to_deformation(name, config):
    modules_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), _MODULES_FOLDER)
    spec = importlib.util.spec_from_file_location(name, join(modules_folder, name + _PYTHON_EXT))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    clazz = getattr(m, name)
    return clazz(config)