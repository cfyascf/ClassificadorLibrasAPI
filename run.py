from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from app.utils import Config, db
from app.controllers.classification import ClassificationController

def setup_app():
    # ..create app.
    app = Flask(__name__)

    # ..config db..
    app.config.from_object(Config)

    # ..implement cors..
    CORS(app, resources={r"/*": {"origins": "*"}})

    # ..initialize database..
    db.init_app(app)
    
    # ..initialize api..
    api = Api(app)

    # ..define routes..
    api.add_resource(ClassificationController, '/classify')

    return app

if __name__ == '__main__': 
    app = setup_app()

    with app.app_context():
        db.create_all()

    app.run(debug=True)