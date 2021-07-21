import igl
import numpy as np


# file = r"D:\Graduate\Master\Projects\Metric - Danial Ritchie\PerceptualMetric\examples\data_out\my_vox_head_test_32.obj"
#
# vertices, faces = igl.read_triangle_mesh(file, np.float64)
# max_v = np.max(faces)
# counter = [0 for i in range(len(vertices))]
# for face in faces:
#     for v in face:
#         counter[v] += 1
# print(set(counter))
import trimesh

from data.ShapeNet import random_shape_net_object, iterate_shape_net
import os
# old_size = np.load("old.npy")
# new_size = np.load("new.npy")
# print(np.min(old_size), np.min(new_size))
min_path = r"D:\Graduate\Master\Projects\Metric - Danial Ritchie\ShapeNetCore.v2\04379243\eb773e1b74c883a070d809fda3b93e7b\models\model_normalized.obj"
max_path = r"D:\Graduate\Master\Projects\Metric - Danial Ritchie\ShapeNetCore.v2\04530566\c79c87dcf17a40f698501ff072a5cd78\models\model_normalized.obj"
# p = random_shape_net_object()
sample_p = r"D:\Graduate\Master\Projects\Metric - Danial Ritchie\ShapeNetCore.v2\03211117\c47998c0a317c60611ea7f12f22c0e84\models\model_normalized.obj"
a = os.path.dirname(sample_p)
b = os.path.basename(sample_p)
# v, f = igl.read_triangle_mesh(p)
# nv, nf = connect_sperate_component(v, f)
# T = trimesh.Trimesh(v, f)
# components = trimesh.graph.connected_components(T.edges, engine='scipy')
# num_of_components = len(components)
# print(p)
# print(num_of_components)

import matplotlib.pyplot as plt

data = np.load("compare.npy")
old_large = []
old_large_size = []
new_large = []
new_large_size = []
bad = []
old = data[0]
new = data[1]

for i, (o, n) in enumerate(zip(old, new)):
    if o == -1:
        bad.append(i)
    elif o > n:
        old_large.append(i)
        old_large_size.append((o, n))
    else:
        new_large.append(i)
        new_large_size.append((o, n))
exit()


print(max(data[0]))
# print(len(data[0]))
# print(2)
# # some random data
face_num = data[0]  # faces


sorted_face_arg = np.argsort(face_num)
pivot = sorted_face_arg[:40000]
pivot = np.sort(pivot)
np.save("pivots", pivot)
print(pivot)
exit()
print(face_num[pivot])
# exit()

print(pivot)
size_num = data[1]  # sizes
print(size_num[pivot])

exit()
x = face_num[:, np.newaxis]

n_bins = 1000


# We can set the number of bins with the `bins` kwarg
plt.hist(face_num, bins=n_bins)

# a, _, _, _ = np.linalg.lstsq(x, size_num)
# m, b = np.polyfit(face_num, size_num, 1)
# print(a)
# print(m, b)
# m = x.argmax()
# x = np.delete(x, m)
# y = np.delete(y, m)
# m = x.argmax()
# x = np.delete(x, m)
# y = np.delete(y, m)


# plt.plot(face_num, size_num, 'ro')
# plt.plot(face_num, a*face_num)
plt.show()
