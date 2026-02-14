import numpy as np


def transform_lidar_to_camera(points, T):
    ones = np.ones((points.shape[0], 1))
    points_h = np.hstack((points[:, :3], ones))
    transformed = (T @ points_h.T).T
    return transformed[:, :3]
