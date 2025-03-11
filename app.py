from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    news_data = None
    
    if request.method == 'POST':
        city = request.form['city']
        
        # Fetch Weather Data
        weather_api_key = os.getenv('WEATHER_API_KEY')
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        weather_response = requests.get(weather_url)
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
        
        # Fetch News Data
        news_api_key = os.getenv('NEWS_API_KEY')
        news_url = f"https://newsapi.org/v2/everything?q={city}&apiKey={news_api_key}"
        news_response = requests.get(news_url)
        if news_response.status_code == 200:
            news_data = news_response.json()['articles'][:5]  # Top 5 articles
    
    return render_template('index.html', weather=weather_data, news=news_data)

if __name__ == '__main__':
    app.run(debug=True) 