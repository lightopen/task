from flask import render_template, url_for
from . import homepage
from ..forms import SignupForm
from .. import bootstrap



@homepage.route("/")
def index():
    return render_template("index.html")


@homepage.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        pass
    return render_template("signup.html", form=form)