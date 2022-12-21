from flask_user import UserMixin
from siwiectech.extensions import db


class Account(db.Model, UserMixin):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))