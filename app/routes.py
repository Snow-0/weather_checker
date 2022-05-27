from app import app
from flask import render_template, request, url_for
from app.weather import get_weather_info


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        city = request.form.get("city")
        result = get_weather_info(city)
        icon_id = ""
        if "Icon" in result:
            icon_id = result["Icon"]
            del result["Icon"]
        is_string = False
        if type(result) is dict:
            return render_template("index.html", result=result, icon=icon_id)
        else:
            is_string = True
            return render_template(
                "index.html", result=result, is_string=is_string, icon=icon_id
            )

        # <!-- <img src="{{ url_for('static',filename='icons' + {{ icon_id }} + '.png')}}" -->
        # <!-- alt="img"> -->
