from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")

def dashboard():

    try:
        with open("data/setups.json") as f:
            setups = json.load(f)
    except:
        setups = []

    return render_template("index.html", setups=setups)

app.run()
