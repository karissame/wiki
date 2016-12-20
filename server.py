import mysql.connector
import config
from data import *
from flask import Flask, render_template, request, redirect

app = Flask("MyWiki")

@app.route("/")
def homepage(methods=["GET"]):
    title = request.args.get('title')
    edit = request.args.get('edit')
    thispage = Page(title)
    content = thispage.getContent()
    return render_template("homepage.html",title=title,content=content,edit=edit)

@app.route("/submit")
def submit(methods=['POST']):
    title=request.form.get('title')
    article = Page(title)
    article.content=request.form.get('content')
    article.author=request.form.get('author')
    article.update()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
