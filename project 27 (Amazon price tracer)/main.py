from bs4 import BeautifulSoup
import requests
import smtplib
my_gmail_email="ibrahimtest2001@gmail.com"
my_password="qtzyfmplqipxldac"
PRODUCT_LINK="https://appbrewery.github.io/instant_pot/"






response=requests.get(PRODUCT_LINK)
data=response.text
soup=BeautifulSoup(data,"html.parser")

full_price = soup.find(class_="a-offscreen").get_text()
no_sign_price=full_price.split("$")[1]

product_title=soup.find(name="h1",id="title")
price=float(no_sign_price)

if price<100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # creating stmp object
        connection.starttls()  # securing the connection
        connection.login(user=my_gmail_email, password=my_password)
        connection.sendmail(from_addr=my_gmail_email,
                            to_addrs="ibrahimtest2002@outlook.com",
                            msg=f"your product{product_title}\nis now {price}\n{PRODUCT_LINK}".encode("utf-8")

                            )