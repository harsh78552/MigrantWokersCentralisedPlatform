import hashlib
from datetime import timedelta
from ..Schemas.PatientSchema.loginSchema import PatientLoginSchema, PatientLoginResponseSchema
from ..Database.Patient.patient_data import PatientDatabase
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from flask_jwt_extended import create_access_token, set_access_cookies

blp = Blueprint('patient login from here', __name__, description='patient login themselves using this api')


@blp.route('/patient/login')
class PatientLogin(MethodView):
    def __init__(self):
        self.patient_db = PatientDatabase()

    @blp.arguments(PatientLoginSchema)
    @blp.response(200, PatientLoginResponseSchema)
    def post(self, data):
        email = data['email']
        password = data['password']
        hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        patient_data = self.patient_db.find_patient(email)
        if patient_data is None:
            abort(404, message='patient not registered or invalid email....Registered yourself first')
        if patient_data and patient_data['password'] == hash_password:
            if patient_data['role'] == 'patient':
                access_token = create_access_token(identity=email,
                                                   additional_claims=({'role': patient_data['role']}),
                                                   expires_delta=timedelta(hours=5))
                return {
                    "message": "Patient login successfully.",
                    "access_token": access_token
                }
            else:
                abort(403, message='not authorised')
        else:
            abort(401, message='invalid password..')
