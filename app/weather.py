import requests


def get_weather_info(city):
    api_key = "2cd79f8ae3fa5cca37f4cfa4ba0add32"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)
    weather_data = response.json()
    # Program ends when given an invalid city
    if weather_data["cod"] == "404":
        return "Invalid city, please try again"
    else:
        num_desc = [
            "City: ",
            "Temperature:  ",
            "Lows: ",
            "Highs: ",
            "Humidity: ",
            "Description: ",
            "Icon"
        ]
        weather_info = [
            weather_data["name"],
            weather_data["main"]["temp"],
            weather_data["main"]["temp_min"],
            weather_data["main"]["temp_max"],
            weather_data["main"]["humidity"],
            weather_data["weather"][0]["description"],
            weather_data["weather"][0]["icon"]

        ]
        weather_info = list(map(str, weather_info))
        res = {num_desc[i]: weather_info[i] for i in range(len(num_desc))}
        return res
