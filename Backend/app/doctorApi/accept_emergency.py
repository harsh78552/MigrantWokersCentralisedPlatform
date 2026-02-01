from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..role_base_authenticator import check_role
from ..Database.Emergency.patientEmergency import PatientEmergencyDatabase
from ..Database.Patient.patient_data import PatientDatabase
from ..Database.Doctor.doctors_data import DoctorDatabase
from .send_mail_accept_emergency import send_email

blp = Blueprint('accept emergency', __name__, description='doctor accept emergency ')


@blp.route('/doctor/accept/emergency')
class DoctorAcceptEmergency(MethodView):
    def __init__(self):
        self.emergency_db = PatientEmergencyDatabase()
        self.patient_db = PatientDatabase()
        self.doctor_db = DoctorDatabase()

    @check_role('doctor')
    @jwt_required(locations=['headers'])
    def post(self):
        email = get_jwt_identity()
        data = request.get_json()
        emergency_id = data['emergency_id']
        patient__id = data['patient_id']
        response = self.emergency_db.deactivate_patient_emergency_status(email, emergency_id)
        patient_data = self.patient_db.find_patient_through_patient_id(patient__id)
        doctor_data = self.doctor_db.find_doctor(email)
        subject = "Doctor Assigned to Your Emergency"
        body = f"""
        Dear {patient_data['full_name']},
            Dr.{doctor_data['full_name']} has been assigned to your emergency.
            Help is on the way. Please stay calm..... 
            Your Emergency_id:{emergency_id}
        Regards,
        Emergency support team
               """
        send_email(patient_data['email'],subject,body)
        return response
