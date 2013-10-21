from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required, length


class CardSubmitForm(Form):
    card_text = TextAreaField('card_text', validators=[Required(), length(max=512)])
    whom = TextField('whom', default=None, validators=[length(max=30)])