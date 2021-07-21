from typing import Dict, Callable, Tuple

import numpy as np
import trimesh
import trimesh.voxel.creation

from module.Deformer import Deformer


NUM_CUBES = "cubes"

XN = 0
XP = 1
YN = 2
YP = 3
ZN = 4
ZP = 5


class VoxelizeDeformer(Deformer):

    @staticmethod
    def _get_six_faces_status(voxel, order):
        pos = voxel.sparse_indices[order]
        x = pos[0]
        y = pos[1]
        z = pos[2]
        m = voxel.matrix
        maxes = [voxel.shape[0]-1, voxel.shape[1]-1, voxel.shape[2]-1]
        status = []
        if pos[0] == 0:
            status.append(True)
        else:
            status.append(not bool(m[x-1, y, z]))
        if pos[0] == maxes[0]:
            status.append(True)
        else:
            status.append(not bool(m[x+1, y, z]))
        if pos[1] == 0:
            status.append(True)
        else:
            status.append(not bool(m[x, y-1, z]))
        if pos[1] == maxes[1]:
            status.append(True)
        else:
            status.append(not bool(m[x, y+1, z]))
        if pos[2] == 0:
            status.append(True)
        else:
            status.append(not bool(m[x, y, z-1]))
        if pos[2] == maxes[2]:
            status.append(True)
        else:
            status.append(not bool(m[x, y, z+1]))
        return status

    @staticmethod
    def _get_face_indices(voxel, order, direction):
        # center = voxel.points[order]
        pos = voxel.sparse_indices[order]
        nx = pos[0]
        px = pos[0] + 1
        ny = pos[1]
        py = pos[1] + 1
        nz = pos[2]
        pz = pos[2] + 1
        face = []
        if direction == XN:
            face.append([nx, ny, nz])
            face.append([nx, py, nz])
            face.append([nx, py, pz])
            face.append([nx, ny, pz])
        elif direction == XP:
            face.append([px, py, nz])
            face.append([px, ny, nz])
            face.append([px, ny, pz])
            face.append([px, py, pz])
        if direction == YN:
            face.append([px, ny, nz])
            face.append([nx, ny, nz])
            face.append([nx, ny, pz])
            face.append([px, ny, pz])
        elif direction == YP:
            face.append([nx, py, nz])
            face.append([px, py, nz])
            face.append([px, py, pz])
            face.append([nx, py, pz])
        if direction == ZN:
            face.append([nx, ny, nz])
            face.append([px, ny, nz])
            face.append([px, py, nz])
            face.append([nx, py, nz])
        elif direction == ZP:
            face.append([nx, py, pz])
            face.append([px, py, pz])
            face.append([px, ny, pz])
            face.append([nx, ny, pz])
        return face

    @staticmethod
    def i_to_d(voxel, i_index):
        minimum = voxel.bounds[0]

        return [minimum[0] + voxel.pitch[0] * i_index[0],
                minimum[1] + voxel.pitch[1] * i_index[1],
                minimum[2] + voxel.pitch[2] * i_index[2]]

    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        xs = v[:, 0]
        ys = v[:, 1]
        zs = v[:, 2]
        min_x = min(xs)
        max_x = max(xs)
        min_y = min(ys)
        max_y = max(ys)
        min_z = min(zs)
        max_z = max(zs)

        x_len = max_x - min_x
        y_len = max_y - min_y
        z_len = max_z - min_z

        largest_len = max(x_len, y_len, z_len)

        size = largest_len / self.config[NUM_CUBES]

        mesh = trimesh.Trimesh(v, f, process=False)
        g = trimesh.voxel.creation.voxelize(mesh, size)
        g = g.fill()

        int_vertices = []
        vox_shape = g.matrix.shape
        corner_shape = (vox_shape[0]+1, vox_shape[1]+1, vox_shape[2]+1)
        track_vertices = np.full(corner_shape, -1)
        curr_order = 0
        new_faces = []
        for i in range(g.filled_count):
            neighbors = self._get_six_faces_status(g, i)
            for j in range(6):
                if neighbors[j]:
                    outer_face = self._get_face_indices(g, i, j)
                    p = []
                    for corner in outer_face:
                        pre_assigned_id = track_vertices[corner[0]][corner[1]][corner[2]]
                        if pre_assigned_id == -1:
                            p_index = curr_order
                            track_vertices[corner[0]][corner[1]][corner[2]] = p_index
                            int_vertices.append(corner)
                            curr_order += 1
                        else:
                            p_index = pre_assigned_id
                        p.append(p_index)
                    new_faces.append([p[2], p[1], p[0]])
                    new_faces.append([p[0], p[3], p[2]])

        new_vertices = [self.i_to_d(g, i) for i in int_vertices]

        # TODO: ACCELERATE
        return np.array(new_vertices), np.array(new_faces)

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        sampler = lambda q: 2 ** np.floor(q * 3 + 5)
        return {NUM_CUBES: sampler}
