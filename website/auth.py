# for the login, logout and sign up
from flask import Blueprint, render_template
from flask.templating import render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html", Text="Hello Mr ", user="Tim")


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
