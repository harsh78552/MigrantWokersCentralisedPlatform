from flask_smorest import Blueprint
from flask.views import MethodView
from ..Schemas.PatientSchema.profileSchema import ProfileSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..Database.Patient.patient_data import PatientDatabase
from ..role_base_authenticator import check_role

blp = Blueprint('patient profile shown', __name__, description='patient seen her profile....')


@blp.route('/patient/profile')
class PatientProfile(MethodView):
    def __init__(self):
        self.patient_data = PatientDatabase()

    @jwt_required(locations=['headers'])
    @check_role('patient')
    @blp.response(200, ProfileSchema)
    def get(self):
        email = get_jwt_identity()
        data = self.patient_data.find_patient(email)
        data.pop('password', None)
        data.pop('_id', None)
        if 'id_number' in data:
            data['id_number'] = 'xxxx-xxxx-' + data['id_number'][-4:]
        return data
