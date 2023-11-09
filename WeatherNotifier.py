import requests
import time
from win10toast import ToastNotifier

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

class WeatherNotification:
    temperature = None
    max = None
    min = None
    humidity = None
    city = None
    country = None
    description = None
    processed_data = {}

    def __init__(self, processed_data):
        self.processed_data = processed_data
        self.description = ['main']['description']
        self.temperature = processed_data['main']['temp']
        self.max = processed_data['main']['temp_max']
        self.min = processed_data['main']['temp_min']
        self.humidity = processed_data['main']['humidity']
        self.city = processed_data['name']
        self.country = processed_data['sys']['country']

    def check_bad_weather(self):
        toaster = ToastNotifier()
        if self.temperature > 32:
            toaster.show_toast("Weather Alert", f"High temperature in {self.city}, {self.country}",
                               duration=10,
                               threaded=True)
            while toaster.notification_active():
                time.sleep(0.005)
        if self.humidity > 70:
            toaster.show_toast("Weather Alert", f"High humidity in {self.city}, {self.country}",
                               duration=10,
                               threaded=True)
            while toaster.notification_active():
                time.sleep(0.005)

def create_id_description_dict():
    id_description_dict = {}
    for i in range(200, 532):
        if i == 200:
            id_description_dict[i] = "thunderstorm with light rain"
        elif i == 201:
            id_description_dict[i] = "thunderstorm with rain"
        elif i == 202:
            id_description_dict[i] = "thunderstorm with heavy rain"
        elif i == 210:
            id_description_dict[i] = "light thunderstorm"
        elif i == 211:
            id_description_dict[i] = "thunderstorm"
        elif i == 212:
            id_description_dict[i] = "heavy thunderstorm"
        elif i == 221:
            id_description_dict[i] = "ragged thunderstorm"
        elif i == 230:
            id_description_dict[i] = "thunderstorm with light drizzle"
        elif i == 231:
            id_description_dict[i] = "thunderstorm with drizzle"
        elif i == 232:
            id_description_dict[i] = "thunderstorm with heavy drizzle"
        elif i == 300:
            id_description_dict[i] = "light intensity drizzle"
        elif i == 301:
            id_description_dict[i] = "drizzle"
        elif i == 302:
            id_description_dict[i] = "heavy intensity drizzle"
        elif i == 310:
            id_description_dict[i] = "light intensity drizzle rain"
        elif i == 311:
            id_description_dict[i] = "drizzle rain"
        elif i == 312:
            id_description_dict[i] = "heavy intensity drizzle rain"
        elif i == 313:
            id_description_dict[i] = "shower rain and drizzle"
        elif i == 314:
            id_description_dict[i] = "heavy shower rain and drizzle"
        elif i == 321:
            id_description_dict[i] = "shower drizzle"
        elif i == 500:
            id_description_dict[i] = "light rain"
        elif i == 501:
            id_description_dict[i] = "moderate rain"
        elif i == 502:
            id_description_dict[i] = "heavy intensity rain"
        elif i == 503:
            id_description_dict[i] = "very heavy rain"
        elif i == 504:
            id_description_dict[i] = "extreme rain"
        elif i == 511:
            id_description_dict[i] = "freezing rain"
        elif i == 520:
            id_description_dict[i] = "light intensity shower rain"
        elif i == 521: