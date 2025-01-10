from . import user
from db import db_connect

from flask import request, render_template, redirect, url_for
import uuid, os
from datetime import datetime, timedelta
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

psycopg2.extras.register_uuid()
load_dotenv()



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
        password = request.form.get("password", None)
        if password:
            password_hash = generate_password_hash(password)
            password = password_hash
        note_encrypted = None
        timer = int(timer)
        date = datetime.now() + timedelta(minutes=timer)

        cur.execute("""
        INSERT INTO notes(unique_id, note, timer, password)
        VALUES(%s, %s, %s, %s)""", (unique_id, note, date, password,))

        conn.commit()
        conn.close()

        link = os.environ.get("URL") + 'viewing/' + str(unique_id)
        return f"ссылка на записку готова: {link}"
    
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
    if note and note[4]:
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
    if not note:
        return "Запись удалена"
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
        return redirect(url_for('index'))
    return "Note error"