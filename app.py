from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_wtf import CSRFProtect

import forms
from db import *
from models import *
from helper import date_format

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'
csrf = CSRFProtect(app)


def create_session(username='', user_id=''):
    session['username'] = username
    session['user_id'] = user_id


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['new_post', 'comics', 'series', 'anime', 'games', 'tecnologia']:
        return redirect(url_for('login'))
    elif 'username' in session and request.endpoint in ['login', 'signup']:
        return redirect(url_for('index'))


@app.after_request
def after_request(response):
    return response


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
        username = form.username.data
        password = form.password.data

        user = Usuario.query.filter_by(user=username).first()
        if user is not None and user.verify_password(password):
            session['username'] = username
            session['user_id'] = user.id_usuario
            return redirect(url_for('index'))
        else:
            error_message = 'Usuario o contraseña incorrectos'
            flash(error_message)

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
        usuarios(form)
        username = form.username.data
        user = Usuario.query.filter_by(user=username).first()
        session['username'] = username
        session['user_id'] = user.id_usuario
        return render_template('index.html', form=form)

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


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')


@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    form = forms.FrmNewPost(request.form)

    if request.method == 'POST' and form.validate():
        id_usuario = session['user_id']
        publicaciones(form, id_usuario=id_usuario)
        return render_template('index.html', form=form)

    return render_template('new_post.html', form=form)


@app.route('/games', methods=['GET'])
def games():
    title = "Juegos"
    posts = Publicacion.query.join(Usuario, Categoria).filter_by(id_categoria=1).add_columns(
        Usuario.user, Publicacion.titulo, Publicacion.fechaPublicacion, Categoria.nombre, Publicacion.content,
        Publicacion.pictures, Publicacion.topic)
    return render_template('games.html', title=title, date_format=date_format, posts=posts)


@app.route('/anime', methods=['GET'])
def anime():
    title = "Anime"
    posts = Publicacion.query.join(Usuario, Categoria).filter_by(id_categoria=2).add_columns(
        Usuario.user, Publicacion.titulo, Publicacion.fechaPublicacion, Categoria.nombre, Publicacion.content,
        Publicacion.pictures, Publicacion.topic)
    return render_template('anime.html', title=title, date_format=date_format, posts=posts)


@app.route('/comics/', methods=['GET'])
@app.route('/comics/<int:page>', methods=['GET'])
def comics(page=1):
    per_page = 10
    title = "Comics"
    posts = Publicacion.query.join(Usuario, Categoria).filter_by(id_categoria=3).add_columns(
        Usuario.user, Publicacion.titulo, Publicacion.fechaPublicacion, Categoria.nombre, Publicacion.content,
        Publicacion.pictures, Publicacion.topic)
    return render_template('comics.html', title=title, posts=posts, date_format=date_format)


@app.route('/series', methods=['GET'])
def series():
    title = "Series"
    posts = Publicacion.query.join(Usuario, Categoria).filter_by(id_categoria=4).add_columns(
        Usuario.user, Publicacion.titulo, Publicacion.fechaPublicacion, Categoria.nombre, Publicacion.content,
        Publicacion.pictures, Publicacion.topic)
    return render_template('series.html', title=title, date_format=date_format, posts=posts)


@app.route('/tecnologia', methods=['GET'])
def tecnologia():
    title = "Tecnologia"
    posts = Publicacion.query.join(Usuario, Categoria).filter_by(id_categoria=5).add_columns(
        Usuario.user, Publicacion.titulo, Publicacion.fechaPublicacion, Categoria.nombre, Publicacion.content,
        Publicacion.pictures, Publicacion.topic)
    return render_template('tecnologia.html', title=title, date_format=date_format, posts=posts)


if __name__ == '__main__':
    csrf.init_app(app)  # initialize CSRF protection

    app.run()
