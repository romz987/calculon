from flask import render_template, request, url_for, redirect 
from calculon_app import app


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/calculate', methods=['POST'])
def calculate():
    pass
    return render_template("index.html")
