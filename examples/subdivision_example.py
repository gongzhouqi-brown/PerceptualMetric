import igl
import numpy as np

from module.deformers.SubdivisionDeformer import SubdivisionDeformer, STEPS


path = r"/home/zgong8/outputs/bird_house.obj"

def max_test():
    v, f = igl.read_triangle_mesh(path, np.float64)
    df = SubdivisionDeformer({STEPS: 1})
    for i in range(20):
        print(i, len(f))
        v, f = df.transform(v, f)

