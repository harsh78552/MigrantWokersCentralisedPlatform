from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required
from ..Database.Patient.patient_data import PatientDatabase
from ..role_base_authenticator import check_role

blp = Blueprint('doctor seen basic patient information', __name__,
                description='this api fetch basic information of patient....')


@blp.route('/doctor/fetch/patient/information')
class DoctorFetchPatientInformation(MethodView):
    def __init__(self):
        self.patient_db = PatientDatabase()

    @jwt_required(locations=['headers'])
    @check_role('doctor')
    def get(self):
        patient_id = request.args.get('patient_id')
        response = self.patient_db.find_patient_through_patient_id(patient_id)
        response_dict = {"patient_id": response['patient_id'], "name": response['full_name'], 'age': response['age'],
                         'gender': response['gender']}
        return response_dict
