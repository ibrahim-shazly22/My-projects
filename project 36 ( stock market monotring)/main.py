import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key=" IVVJ39Y8ZVI4HKTR"
news_api="5c025289768141a882fbb4fa40891f08"
twilio_recovery_code="5PHDRTV4EVE3S5V5NTC59AC1"
tw_num="+12162450714"
auth_tkoen="4c3e9122f1a1f5f00311e38b8495f01f"
acc_sid="AC5644f776ce0c881d1420caabd03516ca"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_parameters={
    "apikey":api_key,
    "symbol":STOCK_NAME,
    "function":"TIME_SERIES_DAILY"

}
response=requests.get(url="https://www.alphavantage.co/query",params=stock_parameters)
print(response.raise_for_status())
yesterday_data=response.json()["Time Series (Daily)"]
print(yesterday_data)

#TODO 2. - Get the day before yesterday's closing stock price
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_data=yesterday_data["4. close"]
the_day_before_data=data_list[1]
the_day_before_closing=the_day_before_data["4. close"]



#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diffrence=abs(float(yesterday_closing_data) - float(the_day_before_closing))
up_down=None
if diffrence>0:
    up_down="⬆️"
else:
    up_down="⬇️"


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage=round((diffrence / float(yesterday_closing_data)) * 100)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage)>2:
    news_params={
        "q":STOCK_NAME,
        "apiKey":news_api,


    }

    new_response = requests.get(NEWS_ENDPOINT, params=news_params)
    print(new_response.raise_for_status())
    news_data=new_response.json()["articles"]
    three_articles=news_data[:3]
    formatted_articles=[f"{STOCK_NAME}: {up_down}{percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}"for article in three_articles]


    client = Client(acc_sid, auth_tkoen)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=tw_num,
            to="01018166007"
        )




