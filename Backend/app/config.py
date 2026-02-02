import os


def configure_app(app):
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['API_TITLE'] = 'PatientCentralisedRecordSystem'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/swagger'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
    app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config['JWT_SECRET_KEY'] ="harsh8926466446jhgsfblsgwogw4lb"
    app.config['SECRET_KEY'] = "HARSH79565hergitgbslvwfcbiew"

    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'

    app.config['API_SPEC_OPTIONS'] = {
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
            }
        },
        "security": [{"bearerAuth": []}]
    }
