from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pymysql
import os


import forms
from config import DevelopmentConfig
from models import *

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)


@app.route('/')
def index():  # put application's code here
    if 'username' in session:
        username = session['username']
        print(username)

    title = "GeekZone"
    return render_template('index.html', title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.FrmLogin(request.form)

    if request.method == 'POST' and form.validate():
        session['username'] = form.email.data

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = forms.FrmSignup(request.form)

    if request.method == 'POST' and form.validate():
        usuario = Usuario(
            correo=form.email.data,
            user=form.username.data,
            password=form.password.data,
            fechaNacimiento=form.fecha_nacimiento.data
        )
        db.session.add(usuario)
        db.session.commit()

    return render_template('signup.html', form=form)


@app.route('/password_reset', methods=['GET', 'POST'])
def password_reset():
    form = forms.FrmPasswordReset(request.form)

    if request.method == 'POST' and form.validate():
        print("Formulario válido")
        print(form.email.data)
    else:
        print("Formulario inválido")

    return render_template('password_reset.html', form=form)


if __name__ == '__main__':
    # csrf.init_app(app)  # initialize CSRF protection

    '''
    db.init_app(app)
    with app.app_context():
        db.create_all()
    '''

    app.run()
