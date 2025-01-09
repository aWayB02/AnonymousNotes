from . import user
from flask import request, render_template, session, redirect, url_for
import uuid

@user.route("/")
def index():
    return render_template("index.html")

@user.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        unique_id = uuid.uuid1()
        note = request.form.get("note")
        timer = request.form.get("timer")
        password = request.form.get("password")
        return redirect(url_for('user.result', id=unique_id))
    return render_template("index.html")

@user.route("/password/<uuid:id>", methods=["GET", "POST"])
def password(id):
    # ищем пользователя с uuid, сверяем с паролем, перенаправляем на viewing
    pass

@user.route("/viewing/<uuid:id>", methods=["GET", "POST"])
def viewing(id):
    pass

@user.route("/result/<uuid:id>")
def result(id):
    return f"""
        Ссылка на приватную записку
        {id}
    """