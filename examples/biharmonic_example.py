import os
from random import random

from pipeline.Pipeline import Pipeline
from module.deformers.BiharmonicDeformer import *

curr_dir = os.path.dirname(os.path.realpath(__file__))
data_in_dir = "data_in"
data_out_dir = "data_out"
file_name = "mc5b_decimation.obj"


def test():
    in_path = os.path.join(curr_dir, data_out_dir, file_name)
    out_path = os.path.join(curr_dir, data_out_dir, "mc5b_biharmonic.obj")

    p = Pipeline(1)
    c = {PIVOTS: np.floor(random() * 4 + 1), FIRST: random(), SECOND: random(), THIRD: random(), FOURTH: random()}
    d = BiharmonicDeformer(c)
    p.plug(d)

    p.process_shape_file(in_path, out_path)
