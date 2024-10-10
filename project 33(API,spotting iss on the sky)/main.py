import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 30.021723
MY_LONG = 30.975333
my_gmail_email="ibrahimtest2001@gmail.com"
my_password="qtzyfmplqipxldac"


def iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if iss_latitude >=(MY_LAT-5) or iss_latitude<=(MY_LAT+5) and iss_longitude >=(MY_LONG-5) or iss_longitude <=(MY_LONG+5):
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now().hour
def is_night():
    if time_now>=sunset and time_now<=sunrise:
        return True
while True:
    time.sleep(60)
    if iss_location() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # creating stmp object
            connection.starttls()  # securing the connection
            connection.login(user=my_gmail_email, password=my_password)
            connection.sendmail(from_addr=my_gmail_email,
                                to_addrs="ibrahimtest2002@outlook.com",
                                msg=f"subject:Look up\n\n iss is on the sky "
                                )








