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
        is_string = False
        icon = result["Icon"] + ".png"
        if type(result) is dict:
            return render_template("index.html", result=result, icon=icon)
        else:
            is_string = True
            return render_template("index.html", result=result, is_string=is_string)
