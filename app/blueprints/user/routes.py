from . import user
from flask import render_template, session
from app.blueprints.user.forms import CreateNote
from app.db import SecretNote
from uuid import uuid4
from app.blueprints.user.utils import get_encryption_key
from cryptography.fernet import Fernet


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
        text = key.encrypt(form.text.data.encode())
        
        return text.decode()


@user.route("/delete")
def deletenote():
    pass


@user.route("/get")
def get_note():
    pass