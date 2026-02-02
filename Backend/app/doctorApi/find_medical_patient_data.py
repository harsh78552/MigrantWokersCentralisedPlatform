from flask import request
from flask_smorest import Blueprint
from flask.views import MethodView
from ..Database.MedicalRecords.prescriptionDatabase import MedicalRecordDatabase
from ..Database.MedicalRecords.mediacalRecordsFiles import MedicalRecordFileDatabase
from ..role_base_authenticator import check_role
from flask_jwt_extended import jwt_required, get_jwt
blp = Blueprint('doctor get all patient records', __name__,
                description='using this api doctor got all medical records of patient....')


@blp.route("/doctor/patient/medical/record")
class DoctorPatientMedicalHistory(MethodView):
    def __init__(self):
        self.patient_data = MedicalRecordDatabase()

    @jwt_required(locations=['headers'])
    @check_role('doctor')
    def get(self):
        patient_id = request.args.get("patient_id")
        response = self.patient_data.find_medical_data(patient_id)
        return response


@blp.route("/doctor/patient/medical/files")
class DoctorPatientMedicalHistory(MethodView):
    def __init__(self):
        self.patient_file_data = MedicalRecordFileDatabase()

    @check_role('doctor')
    @jwt_required(locations=['headers'])
    def get(self):
        patient_id = request.args.get("patient_id")
        response = self.patient_file_data.find_patient_medical_files(patient_id)
        return response
