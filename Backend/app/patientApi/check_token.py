from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

blp = Blueprint('auth_check', __name__, description='check token validity')


@blp.route('/check/token')
@jwt_required(locations=['headers'])
def check_token():
    return {'message': 'token valid'}, 200
