from flask import render_template, flash
from cardsubmitter import app, models
from cardsubmitter.forms import CardSubmitForm
from cardsubmitter.models import DuplicateCardException


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
            models.Card.create_card(form.card_text.data, user, app.config['PICK_DELIMITER'])
            flash('Hooray and thanks {}!'.format(user.name))
        except DuplicateCardException:
            flash("Sorry! We already have that card")
    return render_template('add.html',
                           title='Contribute Cards',
                           form=form,
                           user=form.whom.data,
                           delimiter=app.config['PICK_DELIMITER'],
                           max_pick=app.config['MAX_PICKS'])
