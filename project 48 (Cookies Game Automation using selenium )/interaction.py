from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",value=True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

#interacting with the webpages

# no_of_articles=driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# no_of_articles.click()
# viewsource=driver.find_element(By.LINK_TEXT,value="Content portals")
# viewsource.click()
# viewsource.send_keys() #to type
# viewsource.send_keys(Keys.ENTER) #to hit enter
first_name=driver.find_element(By.NAME,value="fName")
first_name.click()
first_name.send_keys("Ibrahim")


last_name=driver.find_element(By.NAME,value="lName")
last_name.click()
last_name.send_keys("samir")

email=driver.find_element(By.NAME,value="email")
email.click()
email.send_keys("ibrahim@gmail.com")
email.send_keys(Keys.ENTER)




