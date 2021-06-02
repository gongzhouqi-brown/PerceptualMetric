import numpy as np

from constant.constant import max_legal_faces, max_output_faces
from module.Deformer import Deformer, get_random_deformation

import igl

from module.Refiner import refine


class Pipeline:

    # TODO: ADD useful debug information output

    def __init__(self, slots):
        self._slots = slots
        self._deformers = []

    def plug(self, d: Deformer):
        assert self._slots > len(self._deformers)
        self._deformers.append(d)

    def is_full(self):
        return self._slots == len(self._deformers)

    def process_shape_file(self, in_file: str, out_file: str):
        assert self.is_full()
        vertices, faces = igl.read_triangle_mesh(in_file, np.float64)
        new_vertices, new_faces = self.process_shape_data(vertices, faces)
        if new_faces is not None:
            if len(new_faces) < max_output_faces:
                igl.write_triangle_mesh(out_file, new_vertices, new_faces)
                return True
        return False

    def process_shape_data(self, vertices, faces):
        assert self.is_full()
        nv, nf = refine(vertices, faces)
        for deformer in self._deformers:
            if len(nf) < max_legal_faces:
                nv, nf = deformer.transform(nv, nf)
            else:
                return None, None
        return nv, nf

    def __str__(self):
        s = ""
        for d in self._deformers:
            s += str(type(d))
            s += " "
            s += str(d.config)
            s += " "
        return s


def run_random_pipeline(in_file, out_file):
    p = None
    while p is None:
        q = np.random.uniform()
        slots = int(np.floor(q * 10 + 1))
        p = Pipeline(slots)
        while not p.is_full():
            p.plug(get_random_deformation())
        p_str = str(p)
        vd = p_str.find("VoxelizeDeformer")
        if vd != -1:
            dd = p_str.find("DecimationDeformer", vd)
            if dd != -1:
                p = None
    success = p.process_shape_file(in_file, out_file)
    if success:
        return p, True
    else:
        return p, False
