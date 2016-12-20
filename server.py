import mysql.connector
import config
from data import *
from flask import Flask, render_template, request, redirect

app = Flask("MyWiki")

@app.route("/",methods=["GET"])
def homepage():
    title = request.args.get('title')
    edit = request.args.get('edit')
    thispage = Page(title)
    content = thispage.getContent()
    return render_template("homepage.html",title=title,content=content,edit=edit)

@app.route("/submitx",methods=['GET','POST'])
def submitx():
    title=request.form.get('title')
    article = Page(title)
    print article.content
    article.content=request.form.get('content')
    print article.content
    print article.author
    article.author=request.form.get('author')
    print article.author
    print article.save()
    return redirect("/?title=%s" % title)

if __name__=="__main__":
    app.run(debug=True)
