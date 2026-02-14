import torch
from .base_pipeline import BasePipeline
from src.utils.calibration import transform_lidar_to_camera


class SensorFusionPipeline(BasePipeline):

    def extract(self, image, lidar):
        return {"image": image, "lidar": lidar}

    def transform(self, data):
        lidar_transformed = transform_lidar_to_camera(
            data["lidar"],
            self.config["T_lidar_to_camera"]
        )

        return {
            "image": data["image"],
            "lidar": lidar_transformed
        }

    def load(self, data):
        return {
            "image_tensor": torch.tensor(data["image"]).permute(2, 0, 1).float(),
            "lidar_tensor": torch.tensor(data["lidar"]).float()
        }
