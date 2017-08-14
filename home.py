from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy

from flask import render_template

import pyrebase
from configs.configs import fbaseconfig as fbcfg
firebase = pyrebase.initialize_app(fbcfg)

db = firebase.database()


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

@app.route('/bookmarks', methods=['GET','POST'])
def bookmarks():
    if request.method == 'POST':
        title = request.json['title']
        url = request.json['url']
        db.child("bookmarks").child(title)
        data = {"url": url}
        db.child("bookmarks").push(data)
    b = db.child("bookmarks").get()
    bookmarks = b.val()
    print(bookmarks)

    bmarkslist = []

    for v in bookmarks:
        x = next(iter(bookmarks[v]['users']))
        bmarks = {
            "title": v,
            "url": bookmarks[v]['users'][x]['url']
                  }
        bmarkslist.append(bmarks)

    return render_template("bookmarks.html", bookmarks=bmarkslist)

if __name__ == "__main__":
    app.run()