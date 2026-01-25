from flask import jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt, unset_jwt_cookies
from .Blocklist import Blocklist

blp = Blueprint('doctor logout', __name__, description='doctor logout using this api')


@blp.route('/doctor/logout')
class DoctorLogout(MethodView):
    @jwt_required(locations=['headers'])
    def post(self):
        jti = get_jwt()['jti']
        Blocklist.add(jti)
        response = jsonify({'message': 'doctor logout successfully...'})
        unset_jwt_cookies(response)
        return response, 200
