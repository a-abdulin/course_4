from dao.model.users import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)


    def get_all(self):
        user_data = self.session.query(User).all()
        return user_data

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        user_d = self.get_one(uid)
        self.session.delete(user_d)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        user.title = user_d.get("username")
        user.description = user_d.get("password")
        user.trailer = user_d.get("role")

        self.session.add(user)
        self.session.commit()

