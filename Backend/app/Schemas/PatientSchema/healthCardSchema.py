from marshmallow import fields, Schema


class PatientHealthCardSchema(Schema):
    full_name = fields.Str()
    patient_id = fields.Str()
    current_address = fields.Str()
    blood_group = fields.Str()
    profile_photo = fields.Str()
