from flask.views import MethodView
from flask_jwt_extended import create_access_token, set_access_cookies
from flask_smorest import Blueprint, abort
from ..Database.Doctor.doctors_data import DoctorDatabase
from ..Schemas.DoctorSchema.DoctorLoginSchema import DoctorLogin,DoctorLoginResponseSchema
import hashlib
from datetime import timedelta

blp = Blueprint(
    "doctor_login",
    __name__,
    description="Doctor login APIs"
)


@blp.route('/doctor/login')
class DoctorLogin(MethodView):
    def __init__(self):
        self.doctor_db = DoctorDatabase()

    @blp.arguments(DoctorLogin)
    @blp.response(200,DoctorLoginResponseSchema)
    def post(self, data):
        email = data['email']
        password = data['password']
        doctor_data = self.doctor_db.find_doctor(email)
        hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if doctor_data:
            if doctor_data['password'] == hash_password:

                if doctor_data['role'] == 'doctor':
                    access_token = create_access_token(identity=email,
                                                       additional_claims=({'role': doctor_data['role']}),
                                                       expires_delta=timedelta(hours=5))
                    return {
                        "message": "Doctor login successfully.",
                        "access_token": access_token
                    }
                else:
                    abort(403, message='not authorised')
            else:
                abort(401, message='incorrect password')
        else:
            abort(404, message='user not found..')
