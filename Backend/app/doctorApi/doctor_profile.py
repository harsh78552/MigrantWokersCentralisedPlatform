from ..Schemas.DoctorSchema.DoctorProfileSchema import DoctorProfileSchema
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import Blueprint
from ..Database.Doctor.doctors_data import DoctorDatabase

blp = Blueprint('doctor profile', __name__, description='doctor fetch profile using this api..')


@blp.route('/doctor/profile')
class DoctorProfile(MethodView):
    def __init__(self):
        self.doctor_db = DoctorDatabase()

    @jwt_required(locations=['headers'])
    @blp.response(200, DoctorProfileSchema)
    def get(self):
        doctor_identity = get_jwt_identity()
        data = self.doctor_db.find_doctor(doctor_identity)
        return data
