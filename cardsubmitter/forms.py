from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required, length, ValidationError


class PickCount(object):
    """
    pick count validator!
    """
    def __init__(self, min=-1, max=-1, delimiter='__', message=None):
        self.min = min
        self.max = max
        self.delimiter = delimiter
        if message is None or message == "":
            message = 'You can only have between {} and {} pick fields'.format(min, max)
        self.message = message

    def __call__(self, form, field):
        l = field.data and field.data.count(self.delimiter) or 0
        if l < self.min or self.max != -1 and l > self.max:
            raise ValidationError(self.message)

pick_count = PickCount


class CardSubmitForm(Form):
    card_text = TextField('card_text', validators=[Required(), length(min=1, max=256), pick_count(max=3, delimiter='__')])
    whom = TextField('whom', default=None, validators=[length(max=30)])
