from . import user
from flask import render_template
from app.user.forms import CreateNote

@user.route("/")
def index():
    form = CreateNote()
    return render_template("index.html", form=form)


@user.route("/create")
def createnote():
    pass


@user.route("/delete")
def deletenote():
    pass