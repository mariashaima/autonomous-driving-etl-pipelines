import numpy as np
from etl.object_detection import ObjectDetectionPipeline

# Fake image
image = np.random.randint(0, 255, (720, 1280, 3), dtype=np.uint8)

pipeline = ObjectDetectionPipeline()
output = pipeline.run(image)

print("Output tensor shape:", output.shape)
