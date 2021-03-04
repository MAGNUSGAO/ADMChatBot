#!/usr/bin/env python3.6
from flask import Flask, render_template, request, redirect, url_for
import main

#core code
app = Flask(__name__)

#if we go to our default domain,,
@app.route("/", methods = ["GET", "POST"])
#what's for home
def home():
	#return render_template("index.html")

    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        text = request.form.get('textbox')
        return render_template("index.html",output = main.chat(text),user_text = text)
    """
    if request.method == "POST":
        text = request.form.get('textbox')
        return render_template("index.html",
        output = backend.meters_feet(float(text)),
        user_text = text)
    """



if __name__ == "__main__":
    app.run()
