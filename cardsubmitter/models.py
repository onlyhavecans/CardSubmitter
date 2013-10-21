from datetime import datetime
from sqlalchemy.exc import IntegrityError

__author__ = 'bitm'

from cardsubmitter import db

WHITE_CARD = 0
BLACK_CARD = 1

PICK_ONE = 1
PICK_TWO = 2
DRAW_TWO_PICK_THREE = 3


class FieldException(Exception):
    pass


class DuplicateCardException(Exception):
    pass


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=True)
    cards = db.relationship('Card', backref='author')

    def __repr__(self):
        return '<Author {}>'.format(self.name)

    @staticmethod
    def get_user(username):
        if username is None or username == "":
            return Author.query.get(1)
        try:
            u = Author(name=username)
            db.session.add(u)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
        return Author.query.filter_by(name=username).first()


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), index=True, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    color = db.Column(db.SmallInteger, default=WHITE_CARD, nullable=False)
    pick_count = db.Column(db.SmallInteger, default=None, nullable=True)

    def __repr__(self):
        return '<Card #{}:{}>'.format(self.id, self.text)

    @staticmethod
    def create_card(card_text, user):
        """
        We abstract this to put in automatic black card creation

        raises: DuplicateCardException if card already exists
        raises: FieldException if there is too many pick fields
        """
        count = card_text.count('__')
        card = Card(text=card_text, author=user)
        if count > 3:
            raise FieldException('Too many pick fields')
        elif count > 0:
            card.color = BLACK_CARD
            card.pick_count = count
        try:
            db.session.add(card)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise DuplicateCardException
