import time
from scheduler import *
from task1 import *
from task2 import *
from task3 import *
from task4 import *
from task5 import *


scheduler = Scheduler()
scheduler.SCH_Init()

task1 = WeatherDataFetcher('Ho Chi Minh City')
task2 = WeatherDatabase()
task3 = AdafruitInterface()
task4 = WeatherNotification()

scheduler.SCH_Add_Task(task1.get_current_data, 1000,1000)
scheduler.SCH_Add_Task(task2.InsertQuery, 1000,1000)
scheduler.SCH_Add_Task(task3.publish_to_adafruit, 5000,500)
scheduler.SCH_Add_Task(task4.check_bad_weather, 5000,10000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)