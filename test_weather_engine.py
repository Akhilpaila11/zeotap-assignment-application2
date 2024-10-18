import pytest
from weather_engine import fetch_weather

def test_fetch_weather():
    result = fetch_weather("Delhi")
    assert result['name'] == "Delhi"
    assert 'main' in result
