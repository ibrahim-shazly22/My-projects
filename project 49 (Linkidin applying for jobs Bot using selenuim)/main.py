import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#from the linkidin main page

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",value=True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/")



#signing in into linkidin
time.sleep(2)
sign_in=driver.find_element(By.XPATH,value='/html/body/nav/div/a[1]')
sign_in.click()
time.sleep(2)
#adding email & password
email_entry=driver.find_element(By.XPATH,value='//*[@id="username"]')
email_entry.send_keys("ibrahimshazly2001@gmail.com")
password_entry=driver.find_element(By.XPATH,value='//*[@id="password"]')
password_entry.click()
password_entry.send_keys("Ihf21122001")
sign_in_button=driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()
time.sleep(5)
#finding the job
jobs_search_bar=driver.find_element(By.XPATH,value='//*[@id="global-nav-typeahead"]/input')
jobs_search_bar.click()
time.sleep(5)
jobs_search_bar.send_keys("python developer")
jobs_search_bar.send_keys(Keys.ENTER)
time.sleep(5)
jobs_button=driver.find_element(By.XPATH,value='//*[@id="search-reusables__filters-bar"]/ul/li[3]/button')
jobs_button.click()
time.sleep(5)
easy_apply=driver.find_element(By.XPATH,value='//*[@id="ember1468"]')
easy_apply.click()
#applying for the job
time.sleep(5)
job_apply=driver.find_element(By.XPATH,value='//*[@id="ember1809"]/span')
job_apply.click()
time.sleep(5)
next_button=driver.find_element(By.XPATH,value='//*[@id="ember1884"]/span')
next_button.click()
time.sleep(5)
next_button.click()
time.sleep(5)
next_button.click()
time.sleep(5)
#reviewing the job offer
review_button=driver.find_element(By.XPATH,value='//*[@id="ember1985"]/span')
review_button.click()

