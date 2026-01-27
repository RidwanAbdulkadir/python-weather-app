from dotenv import load_dotenv
from pprint import pprint
import os   
import requests

load_dotenv()

def get_weather(city):
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: WEATHER_API_KEY not found in .env file.")
        return None
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    weather_data = requests.get(base_url, params=params)
    if weather_data.status_code == 200:
        return weather_data.json()
    else:
        print(f"API Error: Status code {weather_data.status_code}, Response: {weather_data.text}")
        return None
    
if __name__ == "__main__":
    print("\n***Current Weather Information***\n")
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    if weather_data:
        pprint(weather_data)
    else:
        print("City not found!")
    

    