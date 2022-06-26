from flask_wtf import FlaskForm
from wtforms import Form, PasswordField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class FrmLogin(Form):
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember = BooleanField()
    submit = SubmitField('Iniciar Sesión')

