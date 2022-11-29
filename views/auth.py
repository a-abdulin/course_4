from flask import request
from flask_restx import Namespace, Resource

from implemented import auth_service, user_service
from service.auth import check_token, generate_jwt

auth_ns = Namespace('auth')

@auth_ns.route('/register/')
class RegisterView(Resource):
    def post(self):
        json_data = request.json
        user = user_service.create(json_data)
        return "Ok", 201, {"new_user": f"/user/{user.id}"}


@auth_ns.route('/login/')
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

