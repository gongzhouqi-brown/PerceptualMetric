import subprocess
from copy import deepcopy

import igl
import trimesh
import numpy as np

from constant.constant import refiner_path, pivot_path, temp_obj
from data.ShapeNet import iterate_shape_net


def refine(v, f):
    """
    Refine the object to ensure the whole object is connected and normalized
    :param v: vertices
    :param f: faces
    :return: refined vertices and faces
    """
    return deepcopy(v), deepcopy(f)


def refine_shape_net():
    pivots = np.load(pivot_path)
    counter = 0
    for i, old_path in enumerate(iterate_shape_net()):
        if i in pivots:
            new_path = old_path.replace("ShapeNetCore.v2", "new_SN")
            manifold_object(old_path, new_path)
            counter += 1
            print(counter)


def manifold_object(in_path, out_path):
    temp_path = temp_obj
    v, f = igl.read_triangle_mesh(in_path)
    size = len(f)
    multiplier = size * 5
    subprocess.run(["./manifold", in_path, temp_path], cwd=refiner_path)
    subprocess.run(["./simplify", "-i", temp_path, "-o", out_path, "-m", "-f", str(multiplier)], cwd=refiner_path)

def count_shape_net_components():
    total = 0
    counter = 0
    for in_file in iterate_shape_net():
        v, f = igl.read_triangle_mesh(in_file, np.float64)

        tm = trimesh.Trimesh(v, f)

        components = trimesh.graph.connected_components(tm.edges, engine='scipy')
        num_of_components = len(components)

        if num_of_components > 1:
            counter += 1
        total += 1
    print(counter, "out of", total)
