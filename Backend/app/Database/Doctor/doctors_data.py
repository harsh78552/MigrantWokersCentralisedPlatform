from pymongo import MongoClient
import hashlib

import uuid


class DoctorDatabase:
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://ht728350_db_user:I5SaLa4wmZE6UeH5@cluster0.matjbtc.mongodb.net/?appName=Cluster0')
        self.db = self.client['PatientCentralisedRecordSystem']
        self.collection = self.db['doctor-data']

    def insert_doctor_data(self, full_name, gender, date_of_birth, mobile_number, email_id, alternate_phone_number,
                           medical_registration_number, medical_council_name, specialization, year_of_experience,
                           hospital_name, department, work_location, userName, password, preferred_language,
                           medical_certificate=None, government_id_proof=None, profile_photo=None):

        hash_password = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
        unique_id = uuid.uuid4().hex[:10].upper()
        doctor_data = {
            'doctor_id': unique_id,
            'full_name': full_name,
            'gender': gender,
            'date_of_birth': date_of_birth,
            'mobile_number': mobile_number,
            'email_id': email_id,
            'alternate_phone_number': alternate_phone_number,
            'medical_registration_number': medical_registration_number,
            'medical_council_name': medical_council_name,
            'specialization': specialization,
            'year_of_experience': year_of_experience,
            'hospital_name': hospital_name,
            'department': department,
            'work_location': work_location,
            'userName': userName,
            'password': hash_password,
            'preferred_language': preferred_language,
            'role': 'doctor',
            'medical_certificate': medical_certificate,
            'government_id_proof': government_id_proof,
            'profile_photo': profile_photo
        }
        response = self.collection.insert_one(doctor_data)
        # print(response)
        # doc = self.collection.find_one({"_id": response.inserted_id})
        # print(doc)
        if response.inserted_id:
            return {'message': 'doctor registered successfully....'}, 200
        else:
            return {'message': 'doctor not registered successfully....'}, 500

    def find_doctor(self, doctor_email):
        doctor_data = self.collection.find_one({'email_id': doctor_email})
        try:
            if doctor_data:
                doctor_data['_id'] = str(doctor_data.get('_id'))
                return doctor_data
            else:
                return None
        except  Exception as error:
            return str(error), 500
