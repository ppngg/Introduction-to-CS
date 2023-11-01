import requests
import time

class WeatherDataFetcher:
    api_key = None
    city = None
    weather_data = None
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city
        self.api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    def fetch_weather_data(self):
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                self.weather_data = response.json()
            else:
                print(f"Failed to retrieve weather information.")
        except requests.exceptions.RequestException as e:
            print(f"Request to OpenWeatherMap API failed: {str(e)}")
    def get_weather_data(self):
        return self.weather_data

# Testing
if __name__ == "__main__":
    test = WeatherDataFetcher("3398195dd8ca7d2f1a38c3f1cc9c7231", "London")
    test.fetch_weather_data()
    data = test.get_weather_data()
    if(data):
        print(data)

    
