import os
import smtplib

from twilio.rest import Client
from flight_data import FlightData


ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

my_email = os.environ.get("EMAIL")
password = os.environ.get("EMAIL_PASS")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")
# class NotificationManager:
#     def __init__(self, flight_data: FlightData):
#         self.flight_data = flight_data
#
#     def send_sms(self):
#         client = Client(ACCOUNT_SID, AUTH_TOKEN)
#         message = client.messages \
#             .create(
#             body=f"Low price alert! Only BGN{self.flight_data.price} to fly from {self.flight_data.origin_city}-{self.flight_data.origin_airport} "
#                  f"to {self.flight_data.destination_city}-{self.flight_data.destination_airport}, from {self.flight_data.out_date} to {self.flight_data.return_data}",
#             from_='+16206340237',
#             to='+359884909880'
#         )
#         print(message.status)

class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
        )

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )