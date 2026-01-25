from werkzeug.exceptions import BadRequest
from flask_smorest import Blueprint
from flask.views import MethodView
from ..Schemas.PatientSchema.registrationSchema import PatientRegistrationFiles, PatientRegistration
from ..Database.Patient.patient_data import PatientDatabase

blp = Blueprint('patient registration', __name__, description="patient registered themselves using this api.. ")


@blp.route('/patient/registration')
class PatientRegistration(MethodView):
    def __init__(self):
        self.patient_data = PatientDatabase()

    @blp.arguments(PatientRegistration, location='form')
    @blp.arguments(PatientRegistrationFiles, location='files')
    def post(self, args, files):
        from ..Config.cloudinary_config import cloudinary
        profile_image = files.get('profile_photo')
        full_name = args.get('full_name')
        email = args.get('email')
        password = args.get('password')
        age = args.get('age')
        gender = args.get('gender')
        mobile_number = args.get('mobile_number')
        current_address = args.get('current_address')
        home_state = args.get('home_state')
        native_language = args.get('native_language')
        work_type = args.get('work_type')
        employer = args.get('employer')
        current_location = args.get('current_location')
        blood_group = args.get('blood_group')
        id_type = args.get('id_type')
        id_number = args.get('id_number')
        if not profile_image:
            raise BadRequest('Image not received...')
        upload_result = cloudinary.uploader.upload(profile_image)
        profile_image_url = upload_result.get('secure_url')
        result = self.patient_data.insert_patient_data(profile_image_url, full_name, email, password, age, gender,
                                                       mobile_number, current_address, home_state, native_language,
                                                       work_type, employer, current_location, id_type, id_number,
                                                       blood_group)
        return result
