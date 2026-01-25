from marshmallow import fields, Schema


class PatientLoginSchema(Schema):
    email = fields.String(required=True, metadata={'message': 'enter your mail id here:'})
    password = fields.String(required=True, metadata={'message': 'enter your pasword here:'})


class PatientLoginResponseSchema(Schema):
    message = fields.Str()
    access_token = fields.Str()
