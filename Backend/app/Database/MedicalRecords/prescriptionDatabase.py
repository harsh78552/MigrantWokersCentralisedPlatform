from datetime import datetime

from pymongo import MongoClient


class MedicalRecordDatabase:
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://ht728350_db_user:I5SaLa4wmZE6UeH5@cluster0.matjbtc.mongodb.net/?appName=Cluster0')
        self.db = self.client['PatientCentralisedRecordSystem']
        self.collection = self.db['patient_medical_data']

    def insert_medical_data(self, doctor_email, patient_id, hospital_name, department, diagnosis, prescription,
                            doctor_notes,
                            tests):
        data = {'doctor_email': doctor_email, 'patient_id': patient_id, 'hospital_name': hospital_name,
                'department': department,
                'date': datetime.utcnow(),
                'diagnosis': diagnosis, 'prescription': prescription,
                'doctor_notes': doctor_notes, 'tests': tests, 'created_at': datetime.utcnow()}
        result = self.collection.insert_one(data)
        if result.inserted_id:
            return {"success": True, 'message': 'patient health records successfully..'}, 200
        else:
            return {'message': 'some errors occurs..'}, 500

    def find_medical_data(self, patient_id):
        if patient_id:
            patient_medical_data = self.collection.find({"patient_id": patient_id}).sort("created_at", -1)
            patient_medical_data_list = []

            for data in patient_medical_data:
                data['_id'] = str(data.get("_id"))
                patient_medical_data_list.append(data)

            if not patient_medical_data_list:
                return {"message": 'No medical records found from this patient_id..'}, 404

            return patient_medical_data_list

