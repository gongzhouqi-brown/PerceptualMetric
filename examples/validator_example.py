import os

from data.ShapeNet import iterate_shape_net
from module.validator.Validator import is_manifold


curr_dir = os.path.dirname(os.path.realpath(__file__))
data_in_dir = "data_in"
data_out_dir = "data_out"
file_name = "head.obj"


def single_test():
    in_path = os.path.join(curr_dir, data_in_dir, file_name)
    print(is_manifold(file=in_path))


def shape_net_test():
    yes = 0
    no = 0
    for file in iterate_shape_net():
        if is_manifold(file=file):
            yes += 1
        else:
            no += 1
    print(yes, no)


if __name__ == '__main__':
    shape_net_test()