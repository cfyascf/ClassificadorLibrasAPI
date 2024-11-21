import io
import os
import joblib
import numpy as np

from PIL import Image

from app.services.base_model import BaseModel

class ImageClassifier(BaseModel):
    __path = fr'{os.path.dirname(os.path.abspath(__file__))}\models\image_classifier.sav'
    __categories = fr'{os.path.dirname(os.path.abspath(__file__))}\models\classes.txt'
    __instance = None

    def __init__(self):
        super().__init__()
        self.__model = joblib.load(self.__path)

    @staticmethod
    def get_instance():
        if(ImageClassifier.__instance is None):
            nn = ImageClassifier()
            ImageClassifier.__instance = nn

        return ImageClassifier.__instance
    
    def process_image(self, image):
        image_stream = io.BytesIO(image.read())
        img_opened = Image.open(image_stream)
        img_array = np.asarray(img_opened)

        return np.expand_dims(img_array, axis=0)

    def get_categories(self):
        with open(self.__categories, 'r') as file:
            alphabet_list = [line.strip() for line in file]

        return alphabet_list
    
    def predict(self, image):
        expanded_img = self.process_image(image)
        pred = self.__model.predict(expanded_img)
        answear = self.get_categories()[np.argmax(pred)]

        return answear