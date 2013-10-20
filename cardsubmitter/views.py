from flask import render_template
from cardsubmitter import app


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html', title='index & about')


@app.route('/add')
def add():
    return render_template('add.html', title='Contribute Cards')
