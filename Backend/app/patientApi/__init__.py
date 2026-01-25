from .registeration import blp as PatientRegistrationBlueprint
from .healthcard import blp as PatientHealthCardBlueprint
from .login import blp as PatientLoginBlueprint
from .check_token import blp as CheckTokenBlueprint
from .profile import blp as PatientProfileBlueprint
from .emergency import blp as PatientEmergencyBlueprint


def register_patient_blueprint(app_api):
    app_api.register_blueprint(PatientRegistrationBlueprint)
    app_api.register_blueprint(PatientHealthCardBlueprint)
    app_api.register_blueprint(PatientLoginBlueprint)
    app_api.register_blueprint(CheckTokenBlueprint)
    app_api.register_blueprint(PatientProfileBlueprint)
    app_api.register_blueprint(PatientEmergencyBlueprint)
