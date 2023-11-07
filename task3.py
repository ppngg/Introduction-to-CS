from flask import Flask, Response, render_template, request
from task1 import WeatherDataFetcher

class EndpointAction(object):
    def __init__(self, action):
        self.action = action
        self.debug=debug

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
        self.app = Flask(name)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET']):
        self.app.add_url_rule(endpoint, endpoint_name, view_func=handler, methods=methods)


    def add_all_endpoints(self):
        # Homepage
        self.add_endpoint(endpoint="/", endpoint_name="index", handler=self.index)

        # Add action endpoints
        self.add_endpoint(endpoint="/", endpoint_name="getweather", handler=self.getweather, methods=['POST', 'GET'])



    def run(self):
        self.app.run(debug=True)

    def index(self):
        if request.method == 'GET':
            error_message = request.args.get('error_message')
            return render_template("index.html")

    def getweather(self):
        if request.method == 'POST':
            city = request.form.get("city")
            try:
                wd = WeatherDataFetcher(city)
                wd.fetch_weather_data()
                data = wd.get_weather_data()
            except TypeError:
                return render_template('index.html', error_message="Cannot find the city, please enter a valid city name.")
            else:
                return render_template("getweather.html", data = data)
        else:
            return "GET"

# Testing
if __name__ == '__main__':
    a = FlaskAppWrapper('wrap')
    a.add_all_endpoints()
    a.run()