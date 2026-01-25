from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_smorest import Api

api = Api()

jwt = JWTManager()
mail = Mail()
