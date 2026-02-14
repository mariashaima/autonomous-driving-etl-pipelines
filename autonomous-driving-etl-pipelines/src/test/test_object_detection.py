import numpy as np
from src.pipelines.object_detection_pipeline import ObjectDetectionPipeline


def test_pipeline_runs():
    config = {"image_size": [640, 384]}
    pipeline = ObjectDetectionPipeline(config)

    fake_image = np.random.randint(0, 255, (720, 1280, 3), dtype=np.uint8)
    output = pipeline.run(fake_image)

    assert output.shape[0] == 3

