from flask import render_template, url_for
from . import homepage


# index页面指向两个功能页
@homepage.route("/")
def index():
    return render_template("index.html")


