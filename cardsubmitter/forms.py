from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required


class CardSubmitForm(Form):
    card_text = TextField('card_text', validators=[Required()])
    whom = TextField('whom', Default=None)