import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/home/chetan/PycharmProjects/Reqres_API/chromedriver")
driver.maximize_window()
driver.implicitly_wait(40)
driver.get("https://www.facebook.com/")
time.sleep(5)
driver. find_element (By.XPATH, "//*[text()='Create New Account']") .click()
time. sleep(3)

day = Select(driver.find_element(By.ID,'day'))
day_list = []
for i in range(len(day.options)-1):
    day.select_by_index(i)
    day_list.append(day.options[i].text)
print("Day Options: ", day_list)

month = Select(driver.find_element(By.ID,'month'))
month_list = []
for i in range(len(month.options)-1):
    month.select_by_index(i)
    month_list.append(month.options[i].text)
print("Month Options: ", month_list)

year = Select(driver.find_element(By.ID,'year'))
year_list = []
for i in range(20):
    year.select_by_index(i)
    year_list.append(year.options[i].text)
print("Year Options: ", year_list)

actions = ActionChains(driver)
driver.find_element(By.T)