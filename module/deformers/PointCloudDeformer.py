from typing import Dict, Callable, Tuple

import numpy as np
import open3d
import trimesh.sample
import trimesh.voxel.creation

from module.Deformer import Deformer


class PointCloudDeformer(Deformer):
    def transform(self, v: np.ndarray, f: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        mesh = trimesh.Trimesh(v, f, process=False)
        normals = mesh.face_normals
        samples, indices = trimesh.sample.sample_surface(mesh, len(f))
        normals = normals[indices]
        normals = open3d.utility.Vector3dVector(normals)
        pcd = open3d.geometry.PointCloud()
        pcd.points = open3d.utility.Vector3dVector(samples)
        pcd.normals = open3d.utility.Vector3dVector(normals)

        new_mesh, _ = open3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd)
        nv = np.array(new_mesh.vertices)
        nf = np.array(new_mesh.triangles)
        return nv, nf

    @staticmethod
    def get_applicable_configs() -> Dict[str, Callable[[float], float]]:
        return {}
