from flask import render_template, flash
from sqlalchemy.exc import IntegrityError
from cardsubmitter import app, models, db
from cardsubmitter.forms import CardSubmitForm


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
            card = models.Card(text=form.card_text.data, author=user)
            db.session.add(card)
            db.session.commit()
            flash('Hooray and thanks!')
        except IntegrityError as e:
            db.session.rollback()
            flash("Sorry! We already have that card")
    return render_template('add.html', title='Contribute Cards', form=form, user=form.whom.data)
