from marshmallow import Schema, fields, validate


class PatientSuggestionsSchema(Schema):
    patient_id = fields.String(
        required=True,
        validate=validate.Length(min=3)
    )
    hospital_name = fields.String(
        required=True,
        validate=validate.Length(min=3)
    )
    department = fields.String(required=True)

    diagnosis = fields.String(
        required=True,
        validate=validate.Length(min=3)
    )

    prescription = fields.String(required=False)

    notes = fields.String(required=False)
    tests = fields.String(required=False)

    report_category = fields.String(required=False)

    report_type = fields.String(required=False)
    report_name = fields.String(required=False)
