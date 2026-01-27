import pprint
from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    weather_data = None
    error_message = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = get_weather(city)
            if weather_data is None:
                error_message = "City not found!"
            elif weather_data.get('cod') != 200:
                error_message = f"Error: {weather_data.get('message', 'Unknown error')}"
    
    return render_template('index.html', weather=weather_data, error=error_message)

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000)




