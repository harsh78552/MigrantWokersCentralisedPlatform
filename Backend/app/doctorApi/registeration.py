from flask.views import MethodView
from flask_smorest import Blueprint
from ..Database.Doctor.doctors_data import DoctorDatabase
from ..Schemas.DoctorSchema.DoctorRegistrationSchema import DoctorRegistration, DoctorFiles

from werkzeug.exceptions import BadRequest

blp = Blueprint('doctor_registration', __name__,
                description='doctor data come from frontend and send to database for registered')


@blp.route('/doctor-registration')
class DoctorRegistration(MethodView):
    def __init__(self):
        self.doctor_data = DoctorDatabase()

    @blp.arguments(DoctorRegistration, location='form')
    @blp.arguments(DoctorFiles, location="files")
    def post(self, args, files):
        from ..Config.cloudinary_config import cloudinary
        full_name = args.get('name')
        gender = args.get('gender')
        date_of_birth = args.get('date_of_birth')
        mobile_number = args.get('mobile_number')
        email_id = args.get('email_id')
        alternate_phone_number = args.get('alternate_phone_number')
        medical_registration_number = args.get('medical_registration_number')
        medical_council_name = args.get('medical_council_name')
        specialization = args.get('specialization')
        year_of_experience = args.get('year_of_experience')
        hospital_name = args.get('working_hospital_name')
        department = args.get('department')
        work_location = args.get('work_location')
        userName = args.get('userName')
        password = args.get('password')
        preferred_language = args.get('preferred_language')
        medical_certificate_image = files.get('medical_certificate_image')
        government_id_proof_image = files.get('government_id_proof_image')
        profile_photo_image = files.get('profile_photo_image')

        if not medical_certificate_image:
            raise BadRequest('Image not received...')
        upload_result = cloudinary.uploader.upload(medical_certificate_image)
        medical_certificate_image_url = upload_result.get('secure_url')

        if not government_id_proof_image:
            raise BadRequest('Image not received...')
        upload_result = cloudinary.uploader.upload(government_id_proof_image)
        id_proof_image_url = upload_result.get('secure_url')

        if not profile_photo_image:
            raise BadRequest('Image not received...')
        upload_result = cloudinary.uploader.upload(profile_photo_image)
        profile_photo_image_url = upload_result.get('secure_url')
        result = self.doctor_data.insert_doctor_data(full_name, gender, date_of_birth, mobile_number, email_id,
                                                     alternate_phone_number, medical_registration_number,
                                                     medical_council_name, specialization, year_of_experience,
                                                     hospital_name, department, work_location, userName, password,
                                                     preferred_language, medical_certificate_image_url,
                                                     id_proof_image_url, profile_photo_image_url)
        return result
