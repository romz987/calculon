from flask import render_template, request, url_for, redirect 
from calculon_app import app
from calculon_app.calculator import Calculon

calc = Calculon()


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/calculate', methods=['POST'])
def calculate():
    tab = request.args.get('tab')
    subtab = request.args.get('subtab')

    if not tab or not subtab:
        return "Invalid request", 400
    
    # Тестим
    result = calc.entry_point(tab, subtab, request.form)
    print(result)
   
    return render_template("index.html", result=result)
