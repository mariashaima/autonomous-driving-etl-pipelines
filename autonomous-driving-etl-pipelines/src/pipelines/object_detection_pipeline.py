import torch
import cv2
from .base_pipeline import BasePipeline


class ObjectDetectionPipeline(BasePipeline):

    def extract(self, image):
        self.logger.info("Extracting image data...")
        return image

    def transform(self, image):
        self.logger.info("Transforming image...")
        image = cv2.resize(image, tuple(self.config["image_size"]))
        image = image / 255.0
        return image

    def load(self, image):
        self.logger.info("Loading image as tensor...")
        tensor = torch.tensor(image).permute(2, 0, 1).float()
        return tensor
