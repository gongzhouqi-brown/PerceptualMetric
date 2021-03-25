import igl
import numpy as np


def is_manifold(file=None, faces=None):
    if file is not None:
        _, faces = igl.read_triangle_mesh(file, np.float64)
    if faces is None:
        print("Specify at least one of the parameters.")
        assert faces is not None
    return igl.extract_manifold_patches(faces)[0] == 1
