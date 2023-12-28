import os

from cs50 import SQL
from flask import Flask, render_template
from tempfile import mkdtemp


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///livestocks.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about_us.html")
def about_us():
    return render_template("about_us.html")

@app.route("/district.html")
def districts():
    data = db.execute("SELECT state_name as STATE, district_name as DISTRICT, cattle as CATTLE, buffalo as BUFFALO, sheep as SHEEP, goat as GOAT, horse as HORSE, pony AS PONY, mule AS MULE, donkey as DONKEY, camel AS CAMEL, total_poultry AS POULTRY FROM livestocks GROUP BY district_name ORDER BY state_name")
    return render_template("/district.html", data=data)

@app.route("/state.html")
def states():
    data = db.execute("SELECT state_name as STATE, district_name as DISTRICT, SUM(cattle) as CATTLE, SUM(buffalo) as BUFFALO, SUM(sheep) as SHEEP, SUM(goat) as GOAT, SUM(horse) as HORSE, SUM(pony) AS PONY, SUM(mule) AS MULE, SUM(donkey) as DONKEY, SUM(camel) AS CAMEL, SUM(total_poultry) AS POULTRY FROM livestocks GROUP BY state_name ORDER BY state_name")
    return render_template("/state.html", data=data)






