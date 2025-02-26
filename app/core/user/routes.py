from . import user
from flask import flash, redirect, url_for, render_template, abort
from .forms import InputPassword, CreateNote
from uuid import uuid4
from app.core import redis


@user.get("/")
def index():
    form = CreateNote()
    return render_template("index.html", form=form)


@user.post("/create")
def create():
    form = CreateNote()
    if form.validate_on_submit():
        text = form.text.data
        password = form.password.data
        minutes = 10 if form.date_remove.data > 10 else form.date_remove.data
        url = str(uuid4())[:50]
        redis.hset(url, mapping={'password': password.encode(), 'text': text.encode()})
        redis.expire(url, minutes)
        return render_template("result.html", 
                            url='http://127.0.0.1:5000/get_password/' + url, 
                            password=password, 
                            minutes=minutes)


@user.post("/input_password")
def input_password():
    form = InputPassword()
    if form.validate_on_submit():
        url = form.url.data
        password = form.password.data
        info = redis.hgetall(url) 
        if info['password'.decode()] == password:
            return render_template("note.html")
        else:
            flash("error password")


@user.get("/get_password/<url>")
def get_password(url):
    try:
        info = redis.hgetall(url) # если url существует
        form = InputPassword()
        return render_template("input_password", form=form)
    except KeyError:
        abort(404)