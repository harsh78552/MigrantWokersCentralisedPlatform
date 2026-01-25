from marshmallow import fields, Schema


class ProfileSchema(Schema):
    full_name = fields.String()
    age = fields.Integer()
    gender = fields.String()
    blood_group = fields.String()
    email = fields.String()
    mobile_number = fields.String()
    current_address = fields.String()
    current_location = fields.String()
    home_state = fields.String()
    native_language = fields.String()
    work_type = fields.String()
    employer = fields.String()
    id_type = fields.String()
    id_number = fields.String()
