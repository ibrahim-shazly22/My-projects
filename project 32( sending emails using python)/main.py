##################### Normal Starting Project ######################
import pandas
import random
import datetime as dt
import smtplib


my_gmail_email="ibrahimtest2001@gmail.com"
my_password="qtzyfmplqipxldac"
date=dt.datetime.now()
current_month=date.month
current_day=date.day
today=(current_month,current_day)

data=pandas.read_csv("birthdays.csv")
new_dict={(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in new_dict:
    person=new_dict[today]
    file_path=f"gg/letter_{random.randint(1,3)}.txt"
    with open(file_path) as f:
        contents=f.read()
        contents=contents.replace("[NAME]",person["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # creating stmp object
            connection.starttls()  # securing the connection
            connection.login(user=my_gmail_email, password=my_password)
            connection.sendmail(from_addr=my_gmail_email,
                                to_addrs=person["email"],
                                msg=f"subject:Happy Birthday\n\n{contents}"
                                )









# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



