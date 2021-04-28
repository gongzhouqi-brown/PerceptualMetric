import numpy as np
from scipy.spatial.transform import Rotation as R

def rMat(theta, phi):
    sample_dir = [np.cos(phi) * np.sin(theta), np.cos(theta), np.sin(phi) * np.sin(theta)]
    y_axis = [0, 1, 0]
    return R.from_rotvec(theta * np.cross(y_axis, sample_dir)).as_matrix()