**🚗 Autonomous Driving Data Pipelines**

Industry-grade ETL (Extract–Transform–Load) pipelines for perception and multi-sensor research in autonomous systems.

Designed for scalable, reproducible, and production-ready preprocessing of multi-modal sensor data including camera, LiDAR, and trajectory annotations.

**📌 Overview**

Modern autonomous systems rely on structured, validated, and synchronized multi-sensor data.
This repository provides modular and extensible data pipelines that convert raw sensor streams into machine learning–ready tensors.

The architecture follows clean software engineering principles:

Separation of concerns (Extract → Transform → Load)

Configuration-driven execution

Calibration-safe transformations

Testability and CI readiness

Dockerized execution

Dataset-agnostic design

**🎯 Supported Research Domains**
1️⃣ Object Detection

Image preprocessing

Bounding box filtering

Tensor conversion

Model-ready dataset outputs

2️⃣ Trajectory Extraction

Time-series parsing

History–future sequence generation

Kinematic feature engineering

Multi-agent compatible representations

3️⃣ Sensor Fusion

Timestamp alignment

Coordinate frame transformation

Calibration-based LiDAR → Camera projection

Multi-modal tensor preparation

**🏗 Architecture**

<img width="255" height="231" alt="image" src="https://github.com/user-attachments/assets/cd4a7d8c-81c9-4b41-92b4-89ea02e0c42f" />

Design Principles

Abstract base pipeline class

Configurable execution via YAML

Logging-enabled workflows

Modular components (extractors / transformers / loaders)

Clean API: pipeline.run(...)

⚙ Configuration-Driven Execution

All pipelines are controlled via YAML configuration files:

Example:

image_size: [640, 384]
normalize: true


This enables:

Reproducibility

Parameter versioning

Dataset switching without code modification

CI-based regression testing

**🧪 Testing**

Unit tests validate:

Shape consistency

Calibration transforms

Tensor outputs

Sequence generation correctness

Run tests with:

pytest tests/

**🐳 Docker Support**

The project is containerized for reproducible deployment.

Build image:

docker build -t autonomous-driving-pipelines -f docker/Dockerfile .


Run container:

docker run autonomous-driving-pipelines

**📊 Dataset Compatibility**

The pipeline design supports integration with:

**KITTI (Detection & Tracking)**

nuScenes

Custom ROS bag exports

Simulation outputs (CARLA, MetaDrive)

Dataset-specific adapters can be implemented without modifying core pipeline logic.

**🚀 Example Usage**
from src.pipelines.object_detection_pipeline import ObjectDetectionPipeline

config = {"image_size": [640, 384]}
pipeline = ObjectDetectionPipeline(config)

output = pipeline.run(image)

print(output.shape)

**🔒 Engineering Standards**

This repository follows industry software engineering practices:

PEP8-compliant code

Logging integration

Config-based runtime control

Dockerized reproducibility

Unit testing coverage

Modular architecture

Clear separation between data logic and ML logic

**📈 Applications**

ADAS perception validation

Multi-sensor research

Trajectory prediction modeling

Safety-critical scenario analysis

Multi-Agent Reinforcement Learning state generation

Autonomous driving simulation pipelines

**🛣 Roadmap**

Planned extensions:

DVC dataset versioning

MLflow experiment tracking

GitHub Actions CI/CD

ROS2 integration

Real-time streaming pipeline support

Multi-agent RL integration

Safety-critical event mining

**📜 License**

MIT License

**💼 How This Looks to Industry**

This repository demonstrates:

Strong data engineering practices

Clean ML system design

Autonomous driving domain understanding

Calibration-safe sensor fusion implementation

Production mindset (Docker + tests + configs)
