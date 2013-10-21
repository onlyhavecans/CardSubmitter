from flask import render_template, flash
from cardsubmitter import app
from cardsubmitter.forms import CardSubmitForm


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html', title='index & about')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CardSubmitForm()
    if form.validate_on_submit():
        flash('Hooray and thanks!')
    return render_template('add.html', title='Contribute Cards', form=form)
