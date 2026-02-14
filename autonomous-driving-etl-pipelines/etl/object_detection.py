

# 📂 etl/object_detection.py

import numpy as np
import torch
import cv2


class ObjectDetectionPipeline:
    def __init__(self, image_size=(640, 384)):
        self.image_size = image_size

    def extract(self, image):
        return image

    def transform(self, image):
        image = cv2.resize(image, self.image_size)
        image = image / 255.0
        return image

    def load(self, image):
        tensor = torch.tensor(image).permute(2, 0, 1).float()
        return tensor

    def run(self, image):
        data = self.extract(image)
        data = self.transform(data)
        return self.load(data)
