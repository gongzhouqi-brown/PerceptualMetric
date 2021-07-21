import os

from data.ShapeNet import iterate_shape_net, random_shape_net_object
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


def random_shape_net_test():
    file = random_shape_net_object()
    print(file)
    print(is_manifold(file=file))


if __name__ == '__main__':
    file_name = "mc{}{}.obj"
    for i in range(10):
        in_path_ori = os.path.join(curr_dir, data_out_dir, file_name.format(i, ""))
        in_path_a = os.path.join(curr_dir, data_out_dir, file_name.format(i, "a"))
        in_path_b = os.path.join(curr_dir, data_out_dir, file_name.format(i, "b"))
        print(i)
        print(is_manifold(file=in_path_ori))
        print(is_manifold(file=in_path_a))
        print(is_manifold(file=in_path_b))