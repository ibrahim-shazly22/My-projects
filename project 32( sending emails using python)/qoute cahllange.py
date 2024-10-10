import smtplib
import datetime as dt
import random
current_date=dt.datetime.now()
my_gmail_email="ibrahimtest2001@gmail.com"
my_password="qtzyfmplqipxldac"
if current_date.weekday()==3:
    with open("quotes.txt")as file:
        my_quotes=file.readlines()
        random_quote=random.choice(my_quotes)

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:  #creating stmp object
        connection.starttls()     #securing the connection
        connection.login(user=my_gmail_email,password=my_password)
        connection.sendmail(from_addr=my_gmail_email,
                            to_addrs="ibrahimtest2002@outlook.com",
                            msg=f"subject:today's quote\n\n{random_quote}"
                            )