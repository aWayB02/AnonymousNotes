from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired


class CreateNote(FlaskForm):
    text = TextAreaField("Текст записки", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    date_remove = IntegerField("Время в минутах", validators=[DataRequired()])
    submit = SubmitField("Отправить")

class InputPassword(FlaskForm):
    pass