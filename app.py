from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '63e7ba6b9cb84c1694dc87d474e75b74'  # Replace with your API key

@app.route('/weather', methods=['POST', 'GET'])
def get_weather():
    if request.method == 'POST':
        data = request.json
        city = data.get('city', 'Delhi')  # Default to 'Delhi' if no city is provided
    else:
        # For GET requests, get city from query parameter
        city = request.args.get('city', 'Delhi')  # Default to 'Delhi'

    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    
    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404
    
    weather_data = response.json()
    return jsonify(weather_data), 200

if __name__ == '__main__':
    app.run(debug=True)
