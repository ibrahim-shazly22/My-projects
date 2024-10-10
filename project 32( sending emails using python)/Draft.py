# import smtplib
# #__________________________________________sending emails using python _____________________________________________
# my_gmail_email="ibrahimtest2001@gmail.com"
# my_password="qtzyfmplqipxldac"
#
with smtplib.SMTP("smtp.gmail.com",port=587) as connection:  #creating stmp object
    connection.starttls()     #securing the connection
    connection.login(user=my_gmail_email,password=my_password)
    connection.sendmail(from_addr=my_gmail_email,
                        to_addrs="ibrahimtest2002@outlook.com",
                        msg="subject:gg\n\nthis is the body"
                        )

 #--------------------------------------------Date and time----------------------------------------------------------
import datetime as dt
current_date=dt.datetime.now()
year=current_date.year
month=current_date.month
day=current_date.day
print(day)
my_birthday=dt.datetime(year=2001,month=12,day=21)



