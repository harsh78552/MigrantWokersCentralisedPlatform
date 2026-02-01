from pymongo import MongoClient
from datetime import datetime


class MedicalRecordFileDatabase:
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://ht728350_db_user:I5SaLa4wmZE6UeH5@cluster0.matjbtc.mongodb.net/?appName=Cluster0')
        self.db = self.client['PatientCentralisedRecordSystem']
        self.collection = self.db['patient_medical_report_data']

    def insert_medical_record_file(self, patient_id, report_category=None, report_types=None,
                                   file_url=None, report_name=None):
        medical_file_data = {'patient_id': patient_id, 'report_category': report_category,
                             'report_types': report_types,
                             'file_url': file_url, 'report_name': report_name, 'created_at': datetime.utcnow()}
        response = self.collection.insert_one(medical_file_data)
        if response.inserted_id:
            return {'message': 'file uploaded successfully...'}, 200
        else:
            return {'message': 'some error occurred...'}, 500

    def find_patient_medical_files(self, patient_id):
        patient_medical_files = self.collection.find({'patient_id': patient_id}).sort('created_at', -1)
        patient_medical_files_list = []
        for files_data in patient_medical_files:
            files_data['_id'] = str(files_data['_id'])
            dict_files_data = {'patient_id': files_data['patient_id'], 'report_category': files_data['report_category'],
                               'report_types': files_data['report_types'],
                               'file_url': files_data['file_url'],
                               'report_name': files_data['report_name'],
                               'created_at': files_data['created_at']}
            patient_medical_files_list.append(dict_files_data)
        if not patient_medical_files_list:
            return {"message": 'No medical files found from this patient_id..'}, 404
        return patient_medical_files_list
