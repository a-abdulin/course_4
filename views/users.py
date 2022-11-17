from flask import request
from flask_restx import Namespace, Resource

from dao.model.users import UserSchema
from implemented import user_service

users_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        output_us = users_schema.dump(all_users)
        return output_us

    def post(self):
        json_data = request.json
        user = user_service.create(json_data)
        return "Ok", 201, {"new_user": f"/user/{user.id}"}


@users_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        res = user_schema.dump(user)
        return res

    def put(self, uid):
        pass

    def delete(self, uid):
        user_data = user_service.delete(uid)
        res = user_schema.dump(user_data)
        return res, 204



