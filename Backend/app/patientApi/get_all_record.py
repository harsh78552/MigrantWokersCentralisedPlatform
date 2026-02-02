from flask import request
from flask_smorest import Blueprint
from flask.views import MethodView
from ..Database.MedicalRecords.prescriptionDatabase import MedicalRecordDatabase
from ..Database.MedicalRecords.mediacalRecordsFiles import MedicalRecordFileDatabase
from flask_jwt_extended import jwt_required

from ..role_base_authenticator import check_role

blp = Blueprint('migrant patient seen medical reports and test files', __name__,
                description='calling this api migrant patient seen medical reports and test files....')


@blp.route('/migrant/patient/medical/reports')
class PatientMedicalReport(MethodView):
    def __init__(self):
        self.patient_db = MedicalRecordDatabase()

    @check_role('patient')
    @jwt_required(locations=['headers'])
    def get(self):
        patient_id = request.args.get("patient_id")
        response = self.patient_db.find_medical_data(patient_id)
        return response


@blp.route('/migrant/patient/report/files')
class PatientReportFiles(MethodView):
    def __init__(self):
        self.patient_file_data = MedicalRecordFileDatabase()

    @check_role('patient')
    @jwt_required(locations=['headers'])
    def get(self):
        patient_id = request.args.get("patient_id")
        response = self.patient_file_data.find_patient_medical_files(patient_id)
        return response
