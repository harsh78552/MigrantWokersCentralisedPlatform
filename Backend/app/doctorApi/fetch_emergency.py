from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required
from ..role_base_authenticator import check_role
from ..Database.Emergency.patientEmergency import PatientEmergencyDatabase

blp = Blueprint('fetch emergency data', __name__, description='doctor fetch active emergency data')


@blp.route('/doctor/active/emergency')
class FetchActiveEmergencyPatient(MethodView):
    def __init__(self):
        self.emergency_data = PatientEmergencyDatabase()

    @check_role('doctor')
    @jwt_required(locations=['headers'])
    def get(self):
        data = self.emergency_data.find_emergency()
        return data
