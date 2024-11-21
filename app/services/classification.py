from app.data.enums import ModelType
from app.services.nn_singledb_model import NNSingleDBModel
from app.services.random_forest_ml_model import RandomForestMLModel
from app.services.andre_nn_model import NNAndreModel
from app.services.svm_ml_model import SVMMLModel
from app.errors.app import AppError

class ClassificationService:
    __single_db_nn_model : NNSingleDBModel
    __random_forest_model: RandomForestMLModel
    __andre_model : NNAndreModel
    __svm_model: SVMMLModel

    def __init__(self):
        self.__single_db_nn_model = NNSingleDBModel.get_instance()
        self.__random_forest_model = RandomForestMLModel.get_instance()
        self.__svm_model = SVMMLModel.get_instance()
        self.__andre_model = NNAndreModel.get_instance()

    @staticmethod
    def classify(data):
        classifier = ClassificationService()
        classification = None

        model_type = data['model_type']
        media = data['file']

        match model_type:
            case ModelType.SINGLE_DB_NN:
                classification = classifier.__single_db_nn_model.predict(media)
            
            case ModelType.RANDOM_FOREST:
                classification = classifier.__random_forest_model.predict(media)
            
            case ModelType.SVM:
                classification = classifier.__svm_model.predict(media)

            case ModelType.ANDRE_NN:
                classification = classifier.__andre_model.predict(media)

            case _:
                raise AppError(403, "Not a valid model type.")

        return classification