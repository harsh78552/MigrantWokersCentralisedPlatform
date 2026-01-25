from marshmallow import Schema, fields


class DoctorProfileSchema(Schema):
    full_name = fields.String(required=True)
    role = fields.String(required=True)
    specialization = fields.String()
    gender = fields.String()
    date_of_birth = fields.String()
    mobile_number = fields.String()
    alternate_phone_number = fields.String()
    email_id = fields.Email()
    preferred_language = fields.String()
    medical_registration_number = fields.String()
    medical_council_name = fields.String()
    experience = fields.Integer()
    hospital_name = fields.String()
    department = fields.String()
    work_location = fields.String()
    medical_certificate = fields.Url()
    government_id_proof = fields.Url()
    profile_photo = fields.Url()
