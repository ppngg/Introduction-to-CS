import time
from scheduler import *
from task2 import *
from task3 import *

scheduler = Scheduler()
scheduler.SCH_Init()

task2 = WeatherDatabase()
task3 = AdafruitInterface()

scheduler.SCH_Add_Task(task2.InsertQuery, 1000,3000)
scheduler.SCH_Add_Task(task3.publish_to_adafruit, 1000,3000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
