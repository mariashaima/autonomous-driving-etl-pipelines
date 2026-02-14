import numpy as np
import torch


class SensorFusionPipeline:
    def __init__(self, T_lidar_to_camera):
        self.T = T_lidar_to_camera

    def extract(self, image, lidar_points):
        return {"image": image, "lidar": lidar_points}

    def transform(self, data):
        ones = np.ones((data["lidar"].shape[0], 1))
        points_h = np.hstack((data["lidar"][:, :3], ones))
        transformed = (self.T @ points_h.T).T[:, :3]

        return {
            "image": data["image"],
            "lidar": transformed
        }

    def load(self, data):
        return {
            "image_tensor": torch.tensor(data["image"]).permute(2, 0, 1).float(),
            "lidar_tensor": torch.tensor(data["lidar"]).float()
        }

    def run(self, image, lidar_points):
        data = self.extract(image, lidar_points)
        data = self.transform(data)
        return self.load(data)
