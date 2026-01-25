from flask import Flask
from flask_cors import CORS

from .doctorApi import register_doctor_blueprint
from .patientApi import register_patient_blueprint
from .config import configure_app
from .extensions import api, jwt, mail


def create_app():
    app = Flask(__name__)
    configure_app(app)
    CORS(
        app,
        resources={
            r"/*": {
                "origins": [
                    "http://127.0.0.1:5000",
                    "http://localhost:63342"
                ]
            }
        },
        supports_credentials=True
    )

    api.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    register_doctor_blueprint(api)
    register_patient_blueprint(api)
    return app
