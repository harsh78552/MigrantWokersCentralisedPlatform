from datetime import datetime
import uuid
from pymongo import MongoClient
from ..Patient.patient_data import PatientDatabase
from ..Doctor.doctors_data import DoctorDatabase


class PatientEmergencyDatabase:
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://ht728350_db_user:I5SaLa4wmZE6UeH5@cluster0.matjbtc.mongodb.net/?appName=Cluster0')
        self.db = self.client['PatientCentralisedRecordSystem']
        self.collection = self.db['emergency_data']
        self.patient_collection = self.db['patient-data']

    def create_emergency(self, email, payload, severity):
        patient_db = PatientDatabase()
        patient = patient_db.find_patient(email)
        patient_id = patient['patient_id']
        unique_id = uuid.uuid4().hex[:10].upper()
        if patient.get('is_in_emergency') is True:
            return {"message": 'Emergency already active'}, 400
        if severity == 'critical':
            severity_priority = 2
        else:
            severity_priority = 1
        emergency_data = {
            'emergency_id': unique_id,
            'patient_id': patient_id,
            'location': {
                'latitude': payload['latitude'],
                'longitude': payload['longitude'],
                'accuracy': payload['accuracy'],
                'timestamp': payload['timestamp'],
            },
            'status': 'active',
            'assigned_doctor_id': None,
            'assigned_hospital_id': None,
            'assigned_ambulance_id': None,
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
            'resolved_at': None,
            'is_notified': False,
            'severity': severity,
            'severity_priority': severity_priority
        }
        self.collection.insert_one(emergency_data)
        self.patient_collection.update_one(
            {'patient_id': patient_id},
            {'$set': {'is_in_emergency': True}}
        )
        return {'message': 'Emergency created successfully...', 'status': 'Active'}, 201

    def find_emergency(self):
        emergency_data = self.collection.find({
            'status': 'active',
            'is_notified': False
        }).sort([
            ('severity_priority', -1),
            ('location.timestamp', -1)
        ])
        result = []
        for data in emergency_data:
            fetched_data = {'patient_id': data['patient_id'], 'emergency_id': data['emergency_id'],
                            'latitude': data['location']['latitude'], 'longitude': data['location']['longitude'],
                            'time': data['location']['timestamp'], 'severity': data['severity']}
            result.append(fetched_data)
        return result

    def deactivate_patient_emergency_status(self, email, emergency_id):
        doctor_db = DoctorDatabase()
        doctor = doctor_db.find_doctor(email)
        doctor_id = doctor['doctor_id']
        self.collection.update_one({'emergency_id': emergency_id}, {
            '$set': {'status': 'assigned', 'assigned_doctor_id': doctor_id}})
        return {'message': 'Doctor assigned successfully Please stay calm. Help is coming.', 'status': 'assigned',
                'assigned_doctor': doctor['full_name']}, 200
