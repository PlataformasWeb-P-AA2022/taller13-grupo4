from flask import Flask, render_template
import requests
import json
from config import user, password

app = Flask(__name__, template_folder='templates')

@app.route("/")
def saludo():
    return "<p>Taller 13 --- Plataformas Web</p>"

@app.route("/losedificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificios",
            auth=(user, password))
    edificios = json.loads(r.content)
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=len(edificios))

@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos",
            auth=(user, password))
    departamentos = json.loads(r.content)
    return render_template("losdepartamentos.html", departamentos=departamentos,
    numero_departamentos=len(departamentos))