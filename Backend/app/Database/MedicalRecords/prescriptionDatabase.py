from pymongo import MongoClient
from datetime import datetime


class MedicalRecordFileDatabase:
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://ht728350_db_user:I5SaLa4wmZE6UeH5@cluster0.matjbtc.mongodb.net/?appName=Cluster0')
        self.db = self.client['PatientCentralisedRecordSystem']
        self.collection = self.db['patient_medical_report_data']

    def insert_medical_record_file(self, patient_id, report_types=None, report_types_others=None, file_url=None):
        medical_file_data = {'patient_id': patient_id, 'report_type': report_types,
                             'report_types_others': report_types_others,
                             'file_url': file_url, 'created_at': datetime.utcnow()}
        response = self.collection.insert_one(medical_file_data)
        if response.inserted_id:
            return {'message': 'file uploaded successfully...'}, 200
        else:
            return {'message': 'some error occurred...'}, 500
