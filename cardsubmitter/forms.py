from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required, length


class CardSubmitForm(Form):
    card_text = TextField('card_text', validators=[Required(), length(min=1, max=256)])
    whom = TextField('whom', default=None, validators=[length(max=30)])