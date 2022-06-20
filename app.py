# Janky Commenting
from flask import Flask, render_template, request, redirect
from os.path import exists
import os
import time
import json
app = Flask(__name__)
print("Janky Commenting")
# check if the database in json exists, if not create one.
if exists("./comments.json"):
    file = open("./comments.json","r")
    names = json.loads(file.read())
    file.close()
else:
    print("Failed to find the comments file, Creating new one")
    names = [1]
    file = open("./comments.json","w")
    file.write(json.dumps(names))
    file.close()

@app.route("/post", methods=["POST"])
def post():
    # first check if the request has the name empty or has spaces if there is only spaces or is empty, redirect back to the main page.
    if request.form['name'] == None or request.form['comment'] == None or request.form['name'] == "" or request.form['comment'] == "" or request.form['name'].isspace() or request.form['comment'].isspace():
        return redirect("/", code=302)
    else:
        if len(request.form['name']) > 21:
            return redirect("/", code=302)
        else:
            names.append({"name":request.form['name'],"comment":request.form['comment'],"date":time.strftime("%d-%m-%Y"),"id":names[0]})
            names[0] += 1
            file = open("./comments.json","w")
            file.write(json.dumps(names))
            file.close()
        return redirect("/", code=302)

# main part, uses templates to render the page.
@app.route("/")
def mainpage(names=names):
    return render_template("index.html", names=names)