from abc import abstractmethod
import os

class BaseModel:
    @abstractmethod
    def process_image(self, image):
        """This method should be overridden by subclasses."""
        pass

    @abstractmethod
    def predict(self, image):
        """This method should be overridden by subclasses."""
        pass