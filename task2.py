from task1 import *

class WeatherDataProcessor:
    data_fetcher = None
    weather_data = {}
    def __init__(self, data_fetcher):
        self.data_fetcher = data_fetcher
        

    def process_weather_data(self):
        self.weather_data['temperature'] = self.data_fetcher['main']['temp']
        self.weather_data['min'] = self.data_fetcher['main']['temp_min']
        self.weather_data['max'] = self.data_fetcher['main']['temp_max']
        self.weather_data['humidity'] = self.data_fetcher['main']['humidity']
        self.weather_data['city'] = self.data_fetcher['name']
        self.weather_data['country'] = self.data_fetcher['sys']['country']
    def weather_data_processed(self):
        return self.weather_data
# Testing
if __name__ == "__main__":
    test = WeatherDataFetcher("3398195dd8ca7d2f1a38c3f1cc9c7231", "London")
    test.fetch_weather_data()
    data = test.get_weather_data()
    test2 = WeatherDataProcessor(data)
    test2.process_weather_data()
    processed = test2.weather_data_processed()
    if(processed):
        print(processed['temperature'])
    