from abc import ABC, abstractmethod
import logging


class BasePipeline(ABC):
    def __init__(self, config: dict):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def extract(self, *args, **kwargs):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def load(self, data):
        pass

    def run(self, *args, **kwargs):
        self.logger.info("Starting pipeline execution...")
        raw_data = self.extract(*args, **kwargs)
        transformed = self.transform(raw_data)
        output = self.load(transformed)
        self.logger.info("Pipeline execution completed.")
        return output
from abc import ABC, abstractmethod
import logging


class BasePipeline(ABC):
    def __init__(self, config: dict):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def extract(self, *args, **kwargs):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def load(self, data):
        pass

    def run(self, *args, **kwargs):
        self.logger.info("Starting pipeline execution...")
        raw_data = self.extract(*args, **kwargs)
        transformed = self.transform(raw_data)
        output = self.load(transformed)
        self.logger.info("Pipeline execution completed.")
        return output
