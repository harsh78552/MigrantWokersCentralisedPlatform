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
                    # Doctor frontend
                    "https://migrant-wokers-centralised-platform-three.vercel.app",

                    # Patient frontend
                    "https://migrant-wokers-centralised-platform-sigma.vercel.app",

                    # Local testing
                    "http://localhost:63342"
                ]
            }
        },
        supports_credentials=False
    )

    api.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)

    register_doctor_blueprint(api)
    register_patient_blueprint(api)

    return app
