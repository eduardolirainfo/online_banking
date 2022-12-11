from flask import render_template, request, session, url_for, redirect, flash

from flask.globals import request

from pybanking.models import Bank

users = {}
print(users)


def index():
    if session.get('logged_in') is not None:
        if 'user' in session:
            print(session['user'])
            money = user.view_money()
            return render_template('index.html', money=money)
        else:
            return render_template("index.html")
    else:
        return redirect(url_for('webui.login_page'))


def login_page():
    global user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['user'] = username
            user = Bank(session['user'])
            flash('Login Successful')
            session['logged_in'] = True
            return render_template('index.html')
        else:
            flash('Username dosent exist or wrong password')
            return render_template('login.html')
    return render_template('login.html')


def register_page():
    if request.method == "POST":
        username = request.form['username']
        if username in users:
            flash('Username already exists')
            return render_template("register.html")
        else:
            password = request.form['password']
            users[username] = password
            flash('User created')
            return render_template("register.html")
    else:
        return render_template("register.html")


def deposit_page():
    if request.method == 'POST':
        amount = request.form['deposit']
        user.deposit(amount)
        flash('Deposit made successfully')
        return render_template('deposit.html')
    else:
        return render_template("deposit.html")


def withdraw_page():
    if request.method == 'POST':
        amount = request.form['withdraw']
        user.withdraw(amount)
        flash('Withdrawal carried out successfully')
        return render_template('withdraw.html')
    else:
        return render_template('withdraw.html')


def transfer_page():
    return render_template("transfer.html")


def history_page():
    return render_template("history.html")


def logout_page():
    session.pop('logged_in', None)
    session.pop('user', None)
    flash('Logout successfully')
    return redirect(url_for('webui.index'))
