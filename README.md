# Autonomous Driving ETL Pipelines

Modular ETL (Extract–Transform–Load) pipelines for research in:

- Object Detection
- Trajectory Extraction
- Sensor Fusion

Designed for autonomous driving research using datasets such as KITTI and nuScenes.

---

## Overview

This project provides structured and reproducible preprocessing pipelines that convert raw multi-modal sensor data into machine learning–ready tensors.

The architecture follows a clean ETL separation:

Extract → Transform → Load

---

## Features

### Object Detection Pipeline
- Image extraction
- LiDAR loading
- Bounding box parsing
- Image normalization
- Tensor conversion

### Trajectory Extraction Pipeline
- Tracking file parsing
- Temporal sequence generation
- History/future splitting
- Tensor dataset creation

### Sensor Fusion Pipeline
- Multi-sensor extraction
- Timestamp alignment
- Coordinate transformation
- Fusion-ready tensor outputs

---

## Installation

```bash
git clone https://github.com/your-username/autonomous-driving-etl-pipelines.git
cd autonomous-driving-etl-pipelines
pip install -r requirements.txt
