import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ACCOUNT_EMAIL="ibrahimshazly2001@gmail.com"
PASSWORD="Ihf21122001"
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",value=True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4029291322&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER")




time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)