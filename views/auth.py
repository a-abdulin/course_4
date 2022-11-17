from flask import request
from flask_restx import Namespace, Resource

from implemented import auth_service
from service.auth import check_token, generate_jwt

auth_ns = Namespace('auth')

@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        user_data = request.json
        token_data = auth_service.get_token(user_data)
        return token_data


    def put(self):
        refresh_token = request.json
        token_data = check_token(refresh_token)
        if not token_data:
            return "Not ok", 403

        return generate_jwt(token_data)

