from flask import render_template
# from pybanking.models import Product


def index():
    hello = "olá mundo"
    return render_template("index.html", hello=hello)


def login_page():
    login_user = "login"
    return render_template("login.html", login=login_user)
