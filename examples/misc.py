import os
import numpy as np
import igl

curr_dir = os.path.dirname(os.path.realpath(__file__))
data_in_dir = "data_in"
file_name = "head.obj"
in_path = os.path.join(curr_dir, data_in_dir, file_name)
v, f = igl.read_triangle_mesh(in_path, np.float64)
xs = v[:, 0]
ys = v[:, 1]
zs = v[:, 2]
min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)
min_z = min(zs)
max_z = max(zs)

x_len = (max_x - min_x) * 0.5
y_len = (max_y - min_y) * 0.5
z_len = (max_z - min_z) * 0.5



x_mid = x_len + min_x
y_mid = y_len + min_y
z_mid = z_len + min_z

print(x_mid, y_mid, z_mid)