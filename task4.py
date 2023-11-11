from flask import Flask, Response, render_template, request, redirect
from task1 import WeatherDataFetcher
from task2 import WeatherDatabase

class EndpointAction(object):
    def __init__(self, action):
        self.action = action

    def __call__(self, *args):
        # Perform the action
        answer = self.action()
        # Create the answer (bundle it in a correctly formatted HTTP answer)
        self.response = Response(answer, status=200, headers={})
        # Send it
        return self.response


class FlaskAppWrapper(object):
    app = None
    def __init__(self, name):
        print('Init task 1!')
        self.app = Flask(name)
        self.current_data = None  

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET']):
        self.app.add_url_rule(endpoint, endpoint_name, view_func=handler, methods=methods)


    def add_all_endpoints(self):
        # Homepage
        self.add_endpoint(endpoint="/", endpoint_name="index", handler=self.index, methods=['POST', 'GET'])

        # Add action endpoints
        self.add_endpoint(endpoint="/history", endpoint_name="history", handler=self.history, methods=['GET'])


    def Run(self):
        self.app.run(debug=False)

    def index(self):
        if request.method == 'POST':
            city = request.form.get("name")
            wd = WeatherDataFetcher(city)
            current = wd.get_current_data()
            forecast = wd.get_forecast_data()
            if(current == None and forecast == None):
                return render_template("index.html", error_message="Cannot find the city, please enter a valid city name.")
            else:
                print(current)
                print(forecast)
                self.current_data = current
                return render_template("index.html", current=current, forecast=forecast)
        else:
            return render_template("index.html")
    def history(self):
        data = WeatherDatabase()
        db = data.FetchQuery()
        return render_template("history.html", db = db)

# Testing
if __name__ == '__main__':
    a = FlaskAppWrapper('wrap')
    a.add_all_endpoints()
    a.Run()