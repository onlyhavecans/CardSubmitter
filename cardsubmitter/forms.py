from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, length, ValidationError, Regexp
from cardsubmitter import app


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


class CardSubmitForm(FlaskForm):
    card_text = StringField('card_text', validators=[DataRequired(),
                                                     length(min=1, max=256),
                                                     pick_count(max=app.config['MAX_PICKS'],
                                                                delimiter=app.config['PICK_DELIMITER'])
                                                     ])
    whom = StringField('whom', default=None, validators=[length(max=30)])


class PaginationForm(FlaskForm):
    post_count = SelectField('Cards per page', choices=[(str(x), x) for x in range(10, 60, 10)], coerce=int, default=20)
