from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO

db = SQLAlchemy()

login_manager = LoginManager()

socketio = SocketIO()

from app.models.user import User
from app.models.task import Task


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


def create_app():

    app = Flask(__name__)

    app.config.from_pyfile("../config.py")

    db.init_app(app)

    login_manager.init_app(app)

    socketio.init_app(app)

    from app.routes.auth import auth
    from app.routes.task import task

    app.register_blueprint(auth)

    app.register_blueprint(task)

    return app