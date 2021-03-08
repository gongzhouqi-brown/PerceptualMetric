import numpy as np

from module.Deformer import Deformer, get_random_deformation

import igl

from module.Refiner import refine


class Pipeline:
    def __init__(self, slots):
        self._slots = slots
        self._deformers = []

    def plug(self, d: Deformer):
        assert self._slots > len(self._deformers)
        self._deformers.append(d)

    def is_full(self):
        return self._slots == len(self._deformers)

    def process_shape_file(self, in_file: str, out_file: str) -> None:
        assert self.is_full()
        vertices, faces = igl.read_triangle_mesh(in_file, np.float64)
        new_vertices, new_faces = self.process_shape_data(vertices, faces)
        igl.write_triangle_mesh(out_file, new_vertices, new_faces)

    def process_shape_data(self, vertices, faces):
        assert self.is_full()
        nv, nf = refine(vertices, faces)
        for deformer in self._deformers:
            nv, nf = deformer.transform(nv, nf)
        return nv, nf


def run_random_pipeline(in_file, out_file):
    q = np.random.uniform()
    slots = int(np.floor(q * 10 + 1))
    p = Pipeline(slots)
    while not p.is_full():
        p.plug(get_random_deformation())
    p.process_shape_file(in_file, out_file)