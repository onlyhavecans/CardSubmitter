__author__ = 'bitm'

from app import db

WHITE_CARD = 0
BLACK_CARD = 1


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __repr__(self):
        return '<Card %r>' % (self.nickname)