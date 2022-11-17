from dao.model.users import User


class AuthDAO:
    def __init__(self, session):
        self.session = session

    def get_by_user(self, user_name):
        user_data = self.session.query(User).filter(User.username == user_name).first()
        return user_data

