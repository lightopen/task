from flask import render_template, url_for
from . import homepage

@homepage.route("/")
def index():
    return render_template("index.html")


