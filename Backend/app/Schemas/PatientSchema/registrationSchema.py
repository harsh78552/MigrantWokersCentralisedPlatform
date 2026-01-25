from marshmallow import fields, Schema


class PatientRegistrationFiles(Schema):
    profile_photo = fields.Raw(required=False, metadata={'description': 'this fields accept files types data:'})


class PatientRegistration(Schema):
    full_name = fields.String(required=True, metadata={'description': 'fill your name here:'})
    email = fields.String(required=True, metadata={'description': 'fill your email here:'})
    password = fields.String(required=True, metadata={'description': 'fill your strong password here:'})
    age = fields.String(required=True, metadata={'description': 'fill your age here:'})
    gender = fields.String(required=True, metadata={'description': 'fill your gender here:'})
    mobile_number = fields.String(required=True, metadata={'description': 'fill your mobile_number here:'})
    current_address = fields.String(required=True, metadata={'description': 'fill your current_address here:'})
    home_state = fields.String(required=True, metadata={'description': 'fill your home_state here:'})
    native_language = fields.String(required=True, metadata={'description': 'fill your native_language here:'})
    work_type = fields.String(required=True, metadata={'description': 'fill your work_type here:'})
    employer = fields.String(required=True)
    current_location = fields.String(required=True, metadata={'description': 'fill your current_location here:'})
    blood_group = fields.String(required=True, metadata={'description': 'fill your blood group here:'})
    id_type = fields.String(required=True, metadata={'description': 'fill your id type here:'})
    id_number = fields.String(required=True, metadata={'description': 'fill your id number here:'})
