from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {"username":"Alejandro"}
    posts = [
        {
            "autor":{"username":"Pablo"},
            "body":"Que le gustan los tacos"
        },
        {
            "autor":{"username":"Carlos"},
            "body":"Que tiene calor"
        }
    ]
    return render_template("index.html", titulo = "Hub", user = user, posts=posts)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_={}".format(form.username.data,form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", titulo = "Iniciar Sesión", form=form)

