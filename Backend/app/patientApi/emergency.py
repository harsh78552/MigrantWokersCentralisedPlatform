from flask_jwt_extended import get_jwt_identity, jwt_required
from ..role_base_authenticator import check_role
from ..Database.Emergency.patientEmergency import PatientEmergencyDatabase
from flask.views import MethodView
from flask_smorest import Blueprint
from ..Schemas.PatientSchema.emergency import PatientEmergencySchema

blp = Blueprint('patient emergency functionality', __name__,
                description='This API allows patients to trigger an emergency alert for rapid medical response....')


@blp.route('/patient/emergency')
class PatientEmergency(MethodView):
    def __init__(self):
        self.patient_db = PatientEmergencyDatabase()

    @check_role('patient')
    @jwt_required(locations=['headers'])
    @blp.arguments(PatientEmergencySchema)
    def post(self, args):
        email = get_jwt_identity()
        payload = {
            'latitude': args.get('latitude'),
            'longitude': args.get('longitude'),
            'accuracy': args.get('accuracy'),
            'timestamp': args.get('timestamp')
        }
        severity = args.get('severity')
        response = self.patient_db.create_emergency(email, payload, severity)
        return response
