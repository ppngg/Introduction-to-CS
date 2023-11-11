import pyodbc
from task1 import WeatherDataFetcher

class WeatherDatabase:
    temperature = None
    min = None
    max = None
    humidity = None
    speed = None
    city = None
    country = None
    description = None
    def __init__(self):
        print('Init task 2!')
        self.conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=D:\WeatherFetcher\WeatherHistory.accdb'  # Replace with path to database
        )
        
    def InsertQuery(self):
        print("Running task 2")
        fetcher = WeatherDataFetcher()
        self.data = fetcher.get_current_data()
        if(self.data):
            # Create a connection and cursor for InsertQuery
            insert_conn = pyodbc.connect(self.conn_str)
            insert_cursor = insert_conn.cursor()

            
            self.temperature = self.data['temperature']
            self.min = self.data['min']
            self.max = self.data['max']
            self.humidity = self.data['humidity']
            self.speed = self.data['speed']
            self.city = self.data['city']
            self.country = self.data['country']
            self.description = self.data['description']
            print("Running task 2!")
            query = """INSERT INTO WeatherHistory (Temperature, Min, Max, Humidity, Speed, City, Country, Description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            insert_cursor.execute(query, (self.temperature, self.min, self.max, self.humidity, self.speed, self.city, self.country, self.description 
                ))
            insert_conn.commit()
            insert_cursor.close()
            insert_conn.close()
            print("Database Updated!")
    
    def FetchQuery(self):
        # Create a connection and cursor for FetchQuery
        fetch_conn = pyodbc.connect(self.conn_str)
        fetch_cursor = fetch_conn.cursor()
        try:
            query = """SELECT * FROM WeatherHistory"""
            fetch_cursor.execute(query)
            records = fetch_cursor.fetchall()
            return records
        except Exception as e:
            print(f"Error fetching records: {str(e)}")
            return None
        finally:
            fetch_cursor.close()
            fetch_conn.close()
    
if __name__ == "__main__":
    wd = WeatherDataFetcher('Ho Chi Minh City')
    processed_data = wd.get_current_data()
    if(processed_data):
        print(processed_data)
    test = WeatherDatabase(processed_data)
    test.InsertQuery()
    data = test.FetchQuery()
    print(data)
