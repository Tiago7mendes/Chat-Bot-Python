import datetime
import random
import requests

def get_time():
    return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."

def get_date():
    return f"Today's date is {datetime.datetime.now().strftime('%d/%m/%Y')}."

def tell_joke():
    jokes = [
        "Why did the computer go to therapy? It had too many bytes of emotional baggage.",
        "Why was the math book sad? Because it had too many problems.",
        "What do you call 8 hobbits? A hobbyte."
    ]
    return random.choice(jokes)

def calculate_expression(expression):
    try:
        result = eval(expression)
        return f"The result is {result}."
    except:
        return "I couldn't calculate that, sorry."

def get_weather(city):
    API_KEY = "5e5ac74c7e419ccbb770f0b668b4c742"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=en"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            return f"Error: {data.get('message', 'Could not retrieve weather info')}."
        if "main" in data:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"The weather in {city.title()} is {desc} with {temp}°C."
        else:
            return "I couldn't get the weather information."
    except Exception as e:
        return f"Error connecting to the weather service: {e}"
