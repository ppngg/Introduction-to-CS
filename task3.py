from Adafruit_IO import MQTTClient
import sys
import time
from task1 import WeatherDataFetcher

class AdafruitInterface:
    aio_key = "aio_fsUk73WZaCwVnNyNCuxUHm3oI3OI"
    aio_username = "boostedvgu"
    aio_feed_id = ['Temperature','Min','Max','Humidity','Speed','Description','City']

    def __init__(self):
        print('Init task 3!')
        self.client = MQTTClient(self.aio_username , self.aio_key)
        (self.client).on_connect = AdafruitInterface.connected
        (self.client).on_disconnect = AdafruitInterface.disconnected
        (self.client).on_message = AdafruitInterface.message
        (self.client).on_subscribe = AdafruitInterface.subscribe
        (self.client).connect()
        (self.client).loop_background()

    def connected(client):
        print('Connected')
        
        
    def subscribe(client , userdata , mid , granted_qos):
        for feeds in AdafruitInterface.aio_feed_id:
            client.subscribe(feeds)
        print('Subscribed...')

    def disconnected(client):
        print('Disconnected from the server...')
        sys.exit (1)

    def message(client , aio_feed_id , payload):
        print('Received data: ' + payload)
    
    def publish_to_adafruit(self):
        fetcher = WeatherDataFetcher()
        self.data = fetcher.get_current_data()
        self.client.publish('Description', self.data['description'])
        self.client.publish('Humidity', self.data['humidity'])
        self.client.publish('Max', self.data['max'])
        self.client.publish('Min', self.data['min'])
        self.client.publish('Speed', self.data['speed'])
        self.client.publish('Temperature', self.data['temperature'])
        self.client.publish('City', self.data['city'])
        print("Data Published To Adafruit!")

if __name__ == '__main__':
    wd = WeatherDataFetcher('Ho Chi Minh City')
    data = wd.get_current_data()
    uploader = AdafruitInterface(data)
    while True:
        uploader.publish_to_adafruit()
        time.sleep(10000)

    


    
