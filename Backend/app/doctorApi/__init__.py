from .registeration import blp as DoctorRegistrationBlueprint
from .doctor_login import blp as DoctorLoginBlueprint
from .doctor_profile import blp as DoctorProfileBlueprint
from .doctor_logout import blp as DoctorLogoutBlueprint
from .fetch_emergency import blp as DoctorFetchActiveEmergency
from .accept_emergency import blp as DoctorAcceptEmergency
from.add_medical_records import blp as AddMedicalRecordsBlueprint


def register_doctor_blueprint(app_api):
    app_api.register_blueprint(DoctorRegistrationBlueprint)
    app_api.register_blueprint(DoctorLoginBlueprint)
    app_api.register_blueprint(DoctorProfileBlueprint)
    app_api.register_blueprint(DoctorLogoutBlueprint)
    app_api.register_blueprint(DoctorFetchActiveEmergency)
    app_api.register_blueprint(DoctorAcceptEmergency)
    app_api.register_blueprint(AddMedicalRecordsBlueprint)
