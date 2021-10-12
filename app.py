from flask import Flask, render_template
from math import *

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("base.html")


@app.route("/abc")
def abc():
    return render_template('abc.html')
