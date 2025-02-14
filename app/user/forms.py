from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, TimeField
from wtforms.validators import DataRequired

class CreateNote(FlaskForm):
    text = TextAreaField("text", validators=[DataRequired()])
    TimeField = TimeField("time", validators=[DataRequired()])
    submit = SubmitField("Отправить")
    