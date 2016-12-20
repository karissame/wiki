import mysql.connector
import config
from data import *
from flask import Flask, render_template, request, redirect

app = Flask("MyWiki")
@app.route('/')
def index():
    pages = Page.getObjects()
    return render_template("index.html",pages=pages)

@app.route("/<page_name>",methods=["GET"])
def homepage(page_name):
    title = Database.escape(page_name)
    edit = request.args.get('edit')
    thispage = Page(title)
    content = thispage.getContent()
    last_modified = thispage.last_modified
    return render_template("homepage.html",title=title,content=content,edit=edit,last_modified=last_modified, author=thispage.author)

@app.route("/submitx",methods=['GET','POST'])
def submitx():
    title=Database.escape(request.form.get('title'))
    article = Page(title)
    print article.content
    article.content=Database.escape(request.form.get('content'))
    print article.content
    print article.author
    article.author=Database.escape(request.form.get('author'))
    print article.author
    print article.save()
    return redirect("/%s" % title)

if __name__=="__main__":
    app.run(debug=True)
