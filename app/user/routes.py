from . import user
from db import db_connect

from flask import request, render_template, redirect, url_for
import uuid
from datetime import datetime, timedelta


@user.route("/")
def index():
    return render_template("index.html")

@user.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        conn = db_connect()
        cur = conn.cursor()

        unique_id = uuid.uuid1()
        note = request.form.get("note")
        timer = int(request.form.get("timer"))
        date = datetime.now() + timedelta(minutes=timer)
        password = request.form.get("password")

        cur.execute("""
        INSERT INTO notes(unique_id, note, timer, password)
        VALUES(%s, %s, %s, %s)""", (unique_id, note, date, password,))

        conn.commit()
        conn.close()

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