from . import user
from db import db_connect

from flask import request, render_template, redirect, url_for
import uuid
from datetime import datetime, timedelta
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash

psycopg2.extras.register_uuid()

@user.route("/")
def index():
    return render_template("index.html")

@user.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        conn = db_connect()
        cur = conn.cursor()
        date = None

        unique_id = uuid.uuid1()
        note = request.form.get("note")
        timer = request.form.get("timer")
        password = request.form.get("password")
        password_hash = generate_password_hash(password)
        note_encrypted = None
        if timer:
            timer = int(timer)
            date = datetime.now() + timedelta(minutes=timer)

        cur.execute("""
        INSERT INTO notes(unique_id, note, timer, password)
        VALUES(%s, %s, %s, %s)""", (unique_id, note, date, password_hash,))

        conn.commit()
        conn.close()

        return redirect(url_for('user.viewing', id=unique_id))
    
    return render_template("index.html")


@user.route("/viewing/<uuid:id>", methods=["GET", "POST"])
def viewing(id):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM notes
    WHERE unique_id = %s;
                """, (id, ))

    note = cur.fetchone()
    if note[4]:
        if request.method == "POST":

            password = request.form.get("password")

            if check_password_hash(note[4], password):
                
                return render_template("result.html", note=note[2], timer=note[3], id=note[1])

        return """
            <form action="" method="post">
                <label for="note">Пароль записки:</label><br>
                <input type="text" id="text" name="password"><br><br>
                <button type="submit">Отправить</button>
            </form>
                """
    
    return render_template("result.html", note=note[2], timer=note[3], id=note[1])



@user.route("/delete/<uuid:id>")
def delete(id):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM notes
    WHERE unique_id = %s;
                """, (id, ))
    note = cur.fetchone()
    if note:
        cur.execute("DELETE FROM notes WHERE unique_id = %s", (id, ))
        conn.commit()
        conn.close()
        return "Note deleted", 200
    return "Note error"