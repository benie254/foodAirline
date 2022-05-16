from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    """
    defines User objects
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'Users {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))