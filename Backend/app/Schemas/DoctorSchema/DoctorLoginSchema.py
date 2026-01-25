from marshmallow import fields, Schema


class DoctorLogin(Schema):
    email = fields.String(required=True, metadata={'description': 'abcd@gmail.com'})
    password = fields.String(required=True, metadata={'description': 'enter your password...'})


class DoctorLoginResponseSchema(Schema):
    message = fields.Str()
    access_token = fields.Str()