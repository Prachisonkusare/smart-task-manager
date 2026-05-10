from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from app import db

from app.models.user import User

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():

    return redirect(url_for("auth.login"))


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")

        email = request.form.get("email")

        password = generate_password_hash(
            request.form.get("password")
        )

        user = User(
            username=username,
            email=email,
            password=password
        )

        db.session.add(user)

        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")

        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            return redirect(url_for("task.dashboard"))

        return "Invalid Email or Password"

    return render_template("login.html")