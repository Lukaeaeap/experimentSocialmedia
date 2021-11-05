# The file where we write how the user navigates trough the site
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# The home page for www.website.com/ the slash means it is the home page since we called it that.


@views.route('/')
def home():
    return render_template("home.html")
