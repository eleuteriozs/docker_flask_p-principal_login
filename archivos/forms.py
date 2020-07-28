from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length


class SignupForm(FlaskForm):
    name = StringField('User name', validators=[DataRequired(), Length(min=3, max=50, message="Nombre Incorrecto")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30, message="Contraseña invalida")])
    apellidos = StringField('Apellidos', validators=[DataRequired(), Length(min=25, max=80, message="Apellidos incorrectos")])
    biografia = StringField('Biografia', validators=[DataRequired(), Length(min=10, max=120, message="Descripcion incorrecta")])
    correo = StringField('Correo', validators=[DataRequired(), Length(min=10, max=120, message="Correo incorrecto")])
    telefono = StringField('Telefono', validators=[DataRequired(), Length(min=10, max=12, message="Telefono incorrecto")])

class LoginForm(FlaskForm):
    name = StringField('User name', validators=[DataRequired(), Length(min=3, max=50, message="Nombre Incorrecto")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30, message="Contraseña invalida")])

class Fpublicacion(FlaskForm):
    publicacion = TextAreaField('Crear publicación', validators=[Length(min=5, max=200)])
