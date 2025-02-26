from flask import Flask
from app.core.config import Config
from redis import Redis

app = Flask(__name__)
app.config.from_object(Config)
redis = Redis()

from app.core.user import user
app.register_blueprint(user)