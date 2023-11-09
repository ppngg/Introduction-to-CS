import pyodbc

class WeatherDatabase:
    def __init__(self, ConnectionStr)
        self.ConnectionStr = ConnectionStr
    
    def InsertQuery(self, WeatherData):
        conn = pyodbc.connect(self.ConnectionStr)
        cursor = conn.cursor()
        query = "INSERT INTO WeatherData (Temperature, Min, Max, Humidity, City, Country, DateTime) " \
                    "VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (
                weather_data['temperature'],
                weather_data['min'],
                weather_data['max'],
                weather_data['humidity'],
                weather_data['city'],
                weather_data['country'],
                weather_data['real_time']
            ))
        conn.commit()
        conn.close()

DPath = '.accdb'
ConnectionStr = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={DPath};'







