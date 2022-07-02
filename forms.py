from wtforms import Form, PasswordField, SubmitField, BooleanField, EmailField
from wtforms import HiddenField, StringField, DateField, TextAreaField, SelectField, MultipleFileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import *


def honeypot_check(form, field):
    if field.data:
        raise ValidationError('Honeypot debe estar vacío')


class FrmLogin(Form):
    username = StringField('Usuario', validators=[DataRequired(message="Escribe un usuario")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Escribe una contraseña")])
    remember = BooleanField()
    login = SubmitField('Iniciar Sesión')
    honeypot = HiddenField('', validators=[honeypot_check])


class FrmSignup(Form):
    email = EmailField('Correo electrónico', validators=[DataRequired(message="Escribe un correo electrónico"),
                                                         Email(message="Escribe un correo electrónico válido")])
    username = StringField('Usuario', validators=[DataRequired(message="Escribe un usuario"), Length(min=3, max=20,
                                                                                                     message="El usuario debe tener entre 3 y 20 caracteres")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Escribe una contraseña"), Length(min=8,
                                                                                                              message="La contraseña debe tener al menos 8 caracteres")])
    confirm_password = PasswordField('Confirmar Contraseña',
                                     validators=[DataRequired(message="Debe confirmar su contraseña"),
                                                 EqualTo('password', message="Las contraseñas deben coincidir")])
    fecha_nacimiento = DateField('Fecha de Nacimiento',
                                 validators=[DataRequired(message="Escribe una fecha de nacimiento")])
    signup = SubmitField('Registrarse')
    honeypot = HiddenField('', validators=[honeypot_check])

    def validate_email(self, field):
        email = field.data
        user = Usuario.query.filter_by(correo=email).first()
        if user is not None:
           raise ValidationError('El correo ya está en uso.')

    def validate_username(self, field):
        username = field.data
        user = Usuario.query.filter_by(user=username).first()
        if user is not None:
           raise ValidationError('El usuario ya está en uso.')


class FrmPasswordReset(Form):
    email = EmailField('Correo electrónico', validators=[DataRequired(message="Escribe un correo electrónico"),
                                                         Email(message="Escribe un correo electrónico válido")])
    submit = SubmitField('Enviar')
    honeypot = HiddenField('', validators=[honeypot_check])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('El correo no existe.')


class FrmNewPost(Form):
    title = StringField('Título', validators=[DataRequired(message="Escribe un título")])
    topic = StringField('Tema', validators=[DataRequired(message="Escribe un tema")])
    content = TextAreaField('Contenido', validators=[DataRequired(message="Escribe un contenido")])
    category = SelectField('Categoría', coerce=int, validators=[DataRequired(message="Selecciona una categoría")])
    pictures = MultipleFileField('Imágenes')
    submit = SubmitField('Publicar')
    honeypot = HiddenField('', validators=[honeypot_check])

    def __init__(self, *args, **kwargs):
        super(FrmNewPost, self).__init__(*args, **kwargs)
        self.category.choices = [(c.id_categoria, c.nombre) for c in Categoria.query.all()]
