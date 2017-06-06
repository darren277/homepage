from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/zerotoapp')
def zerotoapp():
    return render_template("zerotoapp.html")

@app.route('/stickynotes')
def stickynotes():
    return render_template("stickynotes.html")

@app.route('/kanban')
def kanban():
    return render_template("kanban.html")

if __name__ == "__main__":
    app.run()