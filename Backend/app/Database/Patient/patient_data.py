from pymongo import MongoClient
import hashlib
import uuid


class PatientDatabase:
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://ht728350_db_user:I5SaLa4wmZE6UeH5@cluster0.matjbtc.mongodb.net/?appName=Cluster0')
        self.db = self.client['PatientCentralisedRecordSystem']
        self.collection = self.db['patient-data']

    def insert_patient_data(self, profile_photo_url, full_name, email, password, age, gender, mobile_number,
                            current_address, home_state,
                            native_language, work_type, employer, current_location, id_type, id_number, blood_group,
                            role='patient'):
        hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        unique_id = uuid.uuid4().hex[:10].upper()

        if len(mobile_number.strip()) == 10 and mobile_number.strip().isdigit():
            if len(id_number.strip()) == 12 and id_number.strip().isdigit():
                patient_data = {
                    'patient_id': unique_id,
                    'profile_photo': profile_photo_url,
                    'full_name': full_name,
                    'email': email,
                    'password': hash_password,
                    'age': age,
                    'gender': gender,
                    'mobile_number': mobile_number,
                    'current_address': current_address,
                    'home_state': home_state,
                    'native_language': native_language,
                    'work_type': work_type,
                    'employer': employer,
                    'current_location': current_location,
                    'id_type': id_type,
                    'id_number': id_number,
                    'role': role,
                    'blood_group': blood_group,
                    'is_in_emergency': False
                }
                response = self.collection.insert_one(patient_data)
                if response.inserted_id:
                    return {'message': 'patient registered successfully....'}, 200
                else:
                    return {'message': 'patient not registered successfully....'}, 500
            else:
                return {'message': 'please insert 12 digit identity number....'}, 400
        else:
            return {'message': 'please insert 10 digit mobile number....'}, 400

    def find_patient(self, email):
        patient_data = self.collection.find_one({'email': email})
        patient_data['_id'] = str(patient_data.get('_id'))
        return patient_data

    def find_patient_through_patient_id(self, patient_id):
        patient_data = self.collection.find_one({'patient_id': patient_id})
        patient_data['_id'] = str(patient_data.get('_id'))
        data = {'email': patient_data['email'], 'name': patient_data['full_name']}
        return data
