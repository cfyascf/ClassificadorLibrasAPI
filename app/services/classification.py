from app.data.enums import ModelType
from app.services.video_classifier import VideoClassifier
from app.services.image_classifier import ImageClassifier
from app.errors.app import AppError

class ClassificationService:
    __video_classifier: VideoClassifier
    __image_classifier: ImageClassifier

    def __init__(self):
        self.__image_classifier = ImageClassifier.get_instance()
        self.__video_classifier = VideoClassifier.get_instance()

    @staticmethod
    def classify(data):
        classifier = ClassificationService()
        classification = None

        model_type = data['model_type']
        media = data['file']

        match model_type:
            case ModelType.VIDEO_CLASSIFIER:
                classification = classifier.__video_classifier.predict(media)
            
            case ModelType.IMAGE_CLASSIFIER:
                classification = classifier.__image_classifier.predict(media)

            case _:
                raise AppError(403, "Not a valid model type.")

        return classification