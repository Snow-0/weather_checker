from app import app
from flask import render_template, request
from app.weather import get_weather_info


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        city = request.form.get("city")
        result = get_weather_info(city)
        return render_template("index.html", result=result)
