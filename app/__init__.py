from flask import Flask
from .user import user


app = Flask(__name__)
app.secret_key = "12345"
app.register_blueprint(user)
