import requests
import json

url = "http://127.0.0.1:5000/weather"
payload = {
    "city": "Delhi"
}
headers = {
    'Content-Type': 'application/json'
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if the response was successful
if response.status_code == 200:
    weather_data = response.json()
    
    # Print the formatted weather data
    print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Feels Like: {weather_data['main']['feels_like']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Pressure: {weather_data['main']['pressure']} hPa")
    print(f"Weather: {weather_data['weather'][0]['description']}")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
