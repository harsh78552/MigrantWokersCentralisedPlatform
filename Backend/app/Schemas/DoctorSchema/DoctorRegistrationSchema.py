from marshmallow import Schema, fields


class DoctorRegistration(Schema):
    name = fields.String(required=True, metadata={'description': 'Enter your name:'})
    gender = fields.String(required=True, metadata={'description': 'Enter your gender:'})
    date_of_birth = fields.String(required=True, metadata={'description': 'Enter your date of birth:'})
    mobile_number = fields.String(required=True, metadata={'description': 'Enter your mobile number:'})
    email_id = fields.String(required=True, metadata={'description': 'Enter your email id:'})
    alternate_phone_number = fields.String(required=True,
                                           metadata={'description': 'Enter your alternate contact number:'})
    medical_registration_number = fields.String(required=True,
                                                metadata={'description': 'Enter your medical registration number :'})
    medical_council_name = fields.String(required=True, metadata={'description': 'Enter medical council name:'})
    specialization = fields.String(required=True, metadata={'description': 'Enter field of specialization:'})
    year_of_experience = fields.Integer(required=True, metadata={'description': 'Enter year of experience:'})
    working_hospital_name = fields.String(required=True, metadata={'description': 'Enter working hospital name:'})
    department = fields.String(required=True, metadata={'description': 'Enter department name:'})
    work_location = fields.String(required=True, metadata={'description': 'Enter work location:'})
    userName = fields.String(required=True, metadata={'description': 'Enter your user name:'})
    password = fields.String(required=True, metadata={'description': 'Enter your password:'})
    preferred_language = fields.String(required=True, metadata={'description': 'Enter your preferred language:'})


class DoctorFiles(Schema):
    medical_certificate_image = fields.Raw(required=False, metadata={'description': 'this fields accept files types data:'})
    government_id_proof_image = fields.Raw(required=False, metadata={'description': 'this fields accept files types data:'})
    profile_photo_image = fields.Raw(required=False, metadata={'description': 'this fields accept files types data:'})
