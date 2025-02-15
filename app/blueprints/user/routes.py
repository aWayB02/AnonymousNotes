from . import user
from flask import render_template, session
from app.blueprints.user.forms import CreateNote
from app.db import SecretNote
from uuid import uuid4
from app.blueprints.user.utils import get_encryption_key


@user.route("/")
def index():
    """
    Функция для отображения главной страницы
    """
    form = CreateNote()
    return render_template("user/index.html", form=form)


@user.post("/create")
def createnote():
    """
    Функция для создания записки
    """
    form = CreateNote()
    if form.validate_on_submit():
        key = get_encryption_key()
        url = uuid4()
        password = uuid4()
        text = form.text.data
        date_remove = form.date_remove.data
        new_note = SecretNote(
            url=(key.encrypt(str(url).encode()).decode()),
            password=(key.encrypt(str(password).encode()).decode()),
            text=(key.encrypt(text.encode()).decode()),
            date_remove=date_remove)
        
        new_note.create_note()

        return render_template('user/result.html', key=session['encryption_key'], url=url, password=password)


@user.route("/delete")
def deletenote():
    pass


@user.route("/get")
def get_note():
    pass

