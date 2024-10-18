import requests

API_KEY = 'your_openweathermap_api_key'  # Replace with your API key

def fetch_weather(city):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    if response.status_code != 200:
        raise ValueError("City not found")
    return response.json()
