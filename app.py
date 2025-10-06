from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def base():
    return render_template('base.html')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/feed")
def feed():
    return render_template('feed.html')

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/login")
def login():
    return render_template('login.html')

app.run(debug=True)