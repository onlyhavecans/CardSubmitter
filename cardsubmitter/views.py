from flask import render_template, flash
from sqlalchemy.exc import IntegrityError
from cardsubmitter import app, models, db
from cardsubmitter.forms import CardSubmitForm
from cardsubmitter.models import DuplicateCardException, FieldException


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html', title='index & about')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CardSubmitForm()
    if form.validate_on_submit():
        user = models.Author.get_user(form.whom.data)
        try:
            models.Card.create_card(form.card_text.data, user)
            flash('Hooray and thanks {}!'.format(user.name))
        except DuplicateCardException:
            flash("Sorry! We already have that card")
        except FieldException:
            flash("Sorry! Draw two, pick three is the most this handles currently")
    return render_template('add.html', title='Contribute Cards', form=form, user=form.whom.data)
