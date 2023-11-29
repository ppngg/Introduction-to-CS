import time
from scheduler import *
from task2 import *
from task3 import *
from task5 import *

scheduler = Scheduler()
scheduler.SCH_Init()

task2 = WeatherDatabase()
task3 = AdafruitInterface()
task5 = EmailSender()

scheduler.SCH_Add_Task(task2.InsertQuery, 1000,7000)
scheduler.SCH_Add_Task(task3.publish_to_adafruit, 1000,7000)
scheduler.SCH_Add_Task(task5.Alert, 1000, 50000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
