import requests
import datetime as dt
MY_LAT=30.021723
MY_LON=30.975333
parameters={
    "lat":MY_LAT,
    "lng":MY_LON,
    "formatted":0

}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])

current_date=dt.datetime
current_hour=current_date.now().hour






