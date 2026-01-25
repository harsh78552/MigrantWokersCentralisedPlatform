from datetime import datetime

from pymongo import MongoClient


class MedicalRecordDatabase:
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://ht728350_db_user:I5SaLa4wmZE6UeH5@cluster0.matjbtc.mongodb.net/?appName=Cluster0')
        self.db = self.client['PatientCentralisedRecordSystem']
        self.collection = self.db['patient_medical_data']

    def insert_medical_data(self, patient_id, doctor_email, diagnosis, prescription, doctor_notes):
        data = {'patient_id': patient_id, 'doctor_email': doctor_email, 'date': datetime.utcnow(),
                'diagnosis': diagnosis, 'prescription': prescription,
                'doctor_notes': doctor_notes, 'created_at': datetime.utcnow()}
        result = self.collection.insert_one(data)
        if result.inserted_id:
            return {'message': 'patient health records successfully..'}, 200
        else:
            return {'message': 'some errors occurs..'}, 500
