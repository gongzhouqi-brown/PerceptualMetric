from typing import Dict, Callable, Tuple

import numpy as np
import open3d
import trimesh.sample
import trimesh.voxel.creation

from module.Deformer import Deformer


class PointCloudDeformer(Deformer):
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        mesh = trimesh.Trimesh(v, f, process=False)
        samples, indices = trimesh.sample.sample_surface(mesh, len(f))
        pcd = open3d.geometry.PointCloud()
        pcd.points = open3d.utility.Vector3dVector(samples)
        pcd.estimate_normals()

        distances = pcd.compute_nearest_neighbor_distance()
        avg_dist = np.average(distances)
        radius = 1.5 * avg_dist

        # new_mesh = open3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
        #     pcd,
        #     open3d.utility.DoubleVector([radius, radius * 2]))
        new_mesh, _ = open3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd)
        nv = np.array(new_mesh.vertices)
        nf = np.array(new_mesh.triangles)
        return nv, nf

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        sampler = lambda q: 2 ** np.floor(q * 3 + 5)
        return {0: sampler}
