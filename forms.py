from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):  # строю форму на основе класса FlaskForm (наследую)
    username = StringField('Имя пользователя: ', validators=[DataRequired])
    password = PasswordField('Пароль: ', validators=[DataRequired])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')