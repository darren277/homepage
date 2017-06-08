from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")

@app.route('/stickynotes')
def stickynotes():
    return render_template("stickynotes.html")

@app.route('/evergraph')
def evergraph():
    return render_template("evergraph.html")

@app.route('/css')
def css():
    return render_template("cssstuff.html")

if __name__ == "__main__":
    app.run()