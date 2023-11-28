import smtplib
import ssl
from email.message import EmailMessage
from task1 import WeatherDataFetcher

class EmailSender:
    subject = None
    body = None
    def __init__(self):
        print("Init task 5!")
        self.email_sender = 'cseboosted@gmail.com'
        self.email_password = 'nypneqzhjvyhvion'
        self.email_receiver = 'phgnguyen92@gmail.com'

        self.bad_weather = ['Thunderstorm', 'Drizzle', 'Rain', 'Snow']
        # Set the subject of the email
        self.subject = 'Weather Alert'

        self.em = EmailMessage()
        self.em['From'] = self.email_sender
        self.em['To'] = self.email_receiver
        self.em['Subject'] = self.subject

    def Alert(self):
        self.body = ""
        fetcher = WeatherDataFetcher()
        self.forecast = fetcher.get_forecast_data()
        for date, data in self.forecast.items():
            # Check if the upcoming weather is
            if any(condition.lower() in data['description'].lower() for condition in self.bad_weather):
                self.body += f"Date: {date}\n"
                self.body += f"Temperature: {data['temperature']}°C\n"
                self.body += f"Description: {data['description']}\n\n"
        # Set the body of the email
        self.em.set_content(self.body)
        # Add SSL (layer of security)
        self.context = ssl.create_default_context()
        # Log in and send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, self.em.as_string())
            print("Email sent!")

if __name__ == '__main__':
    test = EmailSender()
    test.Alert()
