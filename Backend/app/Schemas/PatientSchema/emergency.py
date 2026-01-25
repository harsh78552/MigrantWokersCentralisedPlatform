from marshmallow import fields, Schema, validate


class PatientEmergencySchema(Schema):
    latitude = fields.Float(
        required=True,
        validate=validate.Range(min=-90, max=90)
    )
    longitude = fields.Float(
        required=True,
        validate=validate.Range(min=-180, max=180)
    )
    accuracy = fields.Float(required=True)
    timestamp = fields.DateTime(required=True)
    severity = fields.String(required=True)
