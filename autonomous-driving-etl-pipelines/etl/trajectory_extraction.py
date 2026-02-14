import pandas as pd
import torch


class TrajectoryPipeline:
    def __init__(self, history=10, future=20):
        self.history = history
        self.future = future

    def extract(self, tracking_file):
        return pd.read_csv(tracking_file)

    def transform(self, df):
        sequences = []
        grouped = df.groupby("object_id")

        for obj_id, group in grouped:
            group = group.sort_values("timestamp")
            positions = group[["x", "y"]].values

            for i in range(len(positions) - self.history - self.future):
                hist = positions[i:i+self.history]
                fut = positions[i+self.history:i+self.history+self.future]
                sequences.append((hist, fut))

        return sequences

    def load(self, sequences):
        dataset = []
        for hist, fut in sequences:
            dataset.append({
                "history": torch.tensor(hist).float(),
                "future": torch.tensor(fut).float()
            })
        return dataset

    def run(self, tracking_file):
        df = self.extract(tracking_file)
        sequences = self.transform(df)
        return self.load(sequences)
