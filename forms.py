from wtforms import Form, PasswordField, SubmitField, BooleanField, EmailField, StringField, DateField
from wtforms import HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


def honeypot_check(form, field):
    if field.data:
        raise ValidationError('Honeypot debe estar vacío')


class FrmLogin(Form):
    email = EmailField('Correo electrónico', validators=[DataRequired(message="Escribe un correo electrónico"),
                                                         Email(message="Escribe un correo electrónico válido")])
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


'''
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
           raise ValidationError('El correo ya está en uso.')
'''


class FrmPasswordReset(Form):
    email = EmailField('Correo electrónico', validators=[DataRequired(message="Escribe un correo electrónico"),
                                                         Email(message="Escribe un correo electrónico válido")])
    submit = SubmitField('Enviar')
    honeypot = HiddenField('', validators=[honeypot_check])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('El correo no existe.')
