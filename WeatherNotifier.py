import requests
import time
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
from task1 import WeatherDataFetcher

class WeatherNotification:
    temperature = None
    max = None
    min = None
    humidity = None
    city = None
    country = None
    description = None
    id = None
    processed_data = {}

    def __init__(self, processed_data):
        self.processed_data = processed_data
        self.description = processed_data['description']
        self.temperature = processed_data['temperature']
        self.max = processed_data['max']
        self.min = processed_data['min']
        self.humidity = processed_data['humidity']
        self.city = processed_data['city']
        self.country = processed_data['country']
        self.id = processed_data['id']

    def check_bad_weather(self):
        toaster = ToastNotifier()
        if (self.temperature > 28 and self.humidity > 50):
            toaster.show_toast("Weather Alert", f"{self.temperature}°C, {self.humidity}% humidity in {self.city}, {self.country}",
                                duration=10,
                                threaded=True)
            while toaster.notification_active():
                time.sleep(0.005)
        elif (self.id >= 200 and self.id < 531):
            toaster.show_toast("Weather Alert", f"{self.description} in {self.city}, {self.country}")


if __name__ == "__main__":
    wd = WeatherDataFetcher('Ho Chi Minh City')
    wd.fetch_weather_data()
    data = wd.get_current_data()
    if(data):
        print(data)
    notif = WeatherNotification(data)
    notif.check_bad_weather()

    
