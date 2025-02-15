from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, TimeField, PasswordField
from wtforms.validators import DataRequired

class CreateNote(FlaskForm):
    text = TextAreaField("text", validators=[DataRequired()])
    date_remove = TimeField("time", validators=[DataRequired()])
    submit = SubmitField("Отправить")
