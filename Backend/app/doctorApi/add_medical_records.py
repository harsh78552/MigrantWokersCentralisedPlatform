from flask import abort, request
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..Database.MedicalRecords.mediacalRecordsFiles import MedicalRecordDatabase
from ..Database.MedicalRecords.prescriptionDatabase import MedicalRecordFileDatabase
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
        try:
            data = PatientSuggestionsSchema().load(raw_data)
        except ValidationError as error:
            return {
                "message": "Validation failed", "errors": error.messages}, 422
        from ..Config.cloudinary_config import cloudinary
        doctor_email = get_jwt_identity()
        patient_id = data['patient_id']
        diagnosis = data['diagnosis']
        prescription = data['prescription']
        notes = data['notes']
        report_types = data['report_type']
        report_types_others = data['report_type_other']
        final_report_type = None
        if report_types:
            if report_types == 'other' and report_types_others:
                final_report_type = report_types_others
            else:
                final_report_type = report_types
        file = request.files.get('report_file')
        file_url = None
        if final_report_type and file and file.filename:
            if not allowed_file(file.filename):
                return {'message': 'Invalid file type..'}, 400
            upload_result = cloudinary.uploader.upload(file, folder='patient_reports',
                                                       public_id=f'{patient_id}_{final_report_type}',
                                                       resource_type='auto')
            file_url = upload_result.get('secure_url')

        response = self.medical_suggestion_db.insert_medical_data(doctor_email, patient_id, diagnosis, prescription,
                                                                  notes)
        if report_types is not None or report_types_others is not None and file is not None:
            response = self.medical_files_db.insert_medical_record_file(patient_id, report_types, report_types_others,
                                                                        file_url)
        return response
