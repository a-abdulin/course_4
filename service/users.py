from dao.users import UserDAO
from service.auth import get_hash, password_check


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        user_d["password"] = get_hash(user_d.get("password"))
        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)


    def password_update(self, user_data):
        user_email = user_data.get("email")
        user_db = self.dao.get_by_email(user_email)

        password_old = user_data.get("password_1")
        password_new_hash = get_hash(user_data.get("password_2"))

        if user_db is None:
            return "User is not exist!", 403
        elif not password_check(password_old, user_db.password):
            return "Password is incorrect", 403

        user = self.dao.password_update(user_db, password_new_hash)

        return user

