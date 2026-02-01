from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..Database.MedicalRecords.prescriptionDatabase import MedicalRecordDatabase
from ..Database.MedicalRecords.mediacalRecordsFiles import MedicalRecordFileDatabase
from ..Schemas.MedicalRecordSchema.medicalRecords import PatientSuggestionsSchema
from .check_file_extensions import allowed_file
from marshmallow import ValidationError

blp = Blueprint(
    "patient_suggestions",
    __name__,
    description="API for doctors to add diagnosis, prescriptions, and medical notes for patients"
)


@blp.route('/doctor/add/patient/diagnosis/prescription/medical_notes')
class PatientSuggestions(MethodView):
    def __init__(self):
        self.medical_suggestion_db = MedicalRecordDatabase()
        self.medical_files_db = MedicalRecordFileDatabase()

    @jwt_required(locations=['headers'])
    def post(self):
        raw_data = request.form.to_dict()
        print(raw_data)
        try:
            data = PatientSuggestionsSchema().load(raw_data)
            print(data)
        except ValidationError as error:
            return {
                "message": "Validation failed", "errors": error.messages}, 422
        from ..Config.cloudinary_config import cloudinary
        doctor_email = get_jwt_identity()
        patient_id = data['patient_id']
        hospital_name = data['hospital_name']
        department = data['department']
        diagnosis = data['diagnosis']
        prescription = data['prescription']
        notes = data['notes']
        tests = data['tests']
        report_category = data['report_category']
        report_types = data['report_type']
        final_report_type = None
        if report_category:
            if report_category == 'other' and report_types == 'other':
                report_name = data['report_name']
                final_report_type = report_name
            else:
                final_report_type = report_category
        file = request.files.get('report_file')
        file_url = None
        if final_report_type and file and file.filename:
            if not allowed_file(file.filename):
                return {'message': 'Invalid file type..'}, 400
            upload_result = cloudinary.uploader.upload(file, folder='patient_reports',
                                                       public_id=f'{patient_id}_{final_report_type}',
                                                       resource_type='auto')
            file_url = upload_result.get('secure_url')

        response = self.medical_suggestion_db.insert_medical_data(doctor_email, patient_id, hospital_name, department,
                                                                  diagnosis,
                                                                  prescription,
                                                                  notes, tests)
        if report_category is not None or report_types is not None and file is not None:
            response = self.medical_files_db.insert_medical_record_file(patient_id, report_category, report_types,
                                                                        file_url,report_name=None)
        return response
