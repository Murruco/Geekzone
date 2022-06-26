from flask import Flask
from flask import render_template

from forms import FrmLogin

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    title = "GeekZone"
    return render_template('index.html', title=title)


@app.route('/login')
def login():
    form = FrmLogin()
    return render_template('login.html', form=form)


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/password_reset')
def password_reset():
    return render_template('password_reset.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
