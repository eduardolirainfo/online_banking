from flask import render_template


def index():
    return render_template("index.html")


def login_page():
    return render_template("login.html")


def register_page():
    return render_template("register.html")


def deposit_page():
    return render_template("deposit.html")


def withdraw_page():
    return render_template("withdraw.html")


def transfer_page():
    return render_template("transfer.html")


def history_page():
    return render_template("history.html")


def logout_page():
    return render_template("logout.html")
