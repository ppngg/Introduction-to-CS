import requests
class WeatherDataFetcher:
    api_key = None
    city = None
    fetch_data = None
    current_data = {}
    forecast_data = {}
    def __init__(self, city = 'Ho Chi Minh City'):
        print('Init task 1!')
        self.api_key = "3398195dd8ca7d2f1a38c3f1cc9c7231"
        self.city = city
        self.current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        self.forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}&units=metric"

    def get_current_data(self):
        print("Running task 1!")
        try:
            response = requests.get(self.current_url)
            if response.status_code == 200:
                self.fetch_data = response.json()
                self.current_data['temperature'] = self.fetch_data['main']['temp']
                self.current_data['min'] = self.fetch_data['main']['temp_min']
                self.current_data['max'] = self.fetch_data['main']['temp_max']
                self.current_data['humidity'] = self.fetch_data['main']['humidity']
                self.current_data['city'] = self.fetch_data['name']
                self.current_data['country'] = self.fetch_data['sys']['country']
                self.current_data['id'] = self.fetch_data["weather"][0]["id"]
                self.current_data['dt'] = self.fetch_data['dt']
                self.current_data['description'] = self.fetch_data['weather'][0]['description']
                self.current_data['main'] = self.fetch_data['weather'][0]['main']
                self.current_data['speed'] = self.fetch_data['wind']['speed']
                self.current_data['icon'] = self.fetch_data['weather'][0]['icon']
                return self.current_data
            else:
                print(f"Failed to retrieve weather information.")
        except requests.exceptions.RequestException as e:
            print(f"Request to OpenWeatherMap API failed: {str(e)}")
    def get_forecast_data(self):
        try:
            response = requests.get(self.forecast_url)
            if response.status_code == 200:
                self.fetch_data = response.json()
                for forecast in self.fetch_data['list']:
                    if '12:00:00' in forecast['dt_txt']:
                        date = forecast['dt_txt'].split(' ')[0]
                        if date not in self.forecast_data:
                            self.forecast_data[date] = {
                                'temperature': forecast['main']['temp'],
                                'min_temp': forecast['main']['temp_min'],
                                'max_temp': forecast['main']['temp_max'],
                                'humidity': forecast['main']['humidity'],
                                'wind_speed': forecast['wind']['speed'],
                                'description': forecast['weather'][0]['description'],
                                'icon': forecast['weather'][0]['icon'],
                                'main' : forecast['weather'][0]['main']
                            }
                return self.forecast_data
            else:
                print(f"Failed to retrieve weather information.")
        except requests.exceptions.RequestException as e:
            print(f"Request to OpenWeatherMap API failed: {str(e)}")
        

# Testing
if __name__ == "__main__":
    test = WeatherDataFetcher("Ho Chi Minh City")
    data = test.get_current_data()
    print("Return value of get_current_data()")
    print(data)
    data2 = test.get_forecast_data()
    print("Return value of get_forecast_data")
    print(data2)

    
