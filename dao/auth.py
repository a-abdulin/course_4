from dao.model.users import User


class AuthDAO:
    def __init__(self, session):
        self.session = session

    def get_by_user(self, user_email):
        user_data = self.session.query(User).filter(User.email == user_email).first()
        return user_data

