from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",value=True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

names=driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a ")
dates=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time ")
events={}

for n in range(len(dates)):
    events[n]={
        "date":dates[n].text,
        "name":names[n].text

    }
print(events)


# first_date=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time').text
# first_name=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a').text
# first_dic={
#     "time":first_date,
#     "name":first_name
# }
#
# second_date=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time').text
# second_name=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/a').text
# second_dic={
#     "time":second_date,
#     "name":second_name
# }
#
# final_dic={
#     "0":first_dic,
#     "1":second_dic
# }
# print(final_dic)
