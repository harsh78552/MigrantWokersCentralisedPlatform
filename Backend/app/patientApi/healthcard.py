from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..Database.Patient.patient_data import PatientDatabase
from ..Schemas.PatientSchema.healthCardSchema import PatientHealthCardSchema

blp = Blueprint('patient health card generated', __name__,
                description='patient health card generated form here using this api')


@blp.route('/patient/health-card')
class PatientHealthCard(MethodView):
    def __init__(self):
        self.patient_db = PatientDatabase()

    @jwt_required(locations=['headers'])
    @blp.response(200, PatientHealthCardSchema)
    def get(self):
        email = get_jwt_identity()
        patient_data = self.patient_db.find_patient(email)
        return patient_data
