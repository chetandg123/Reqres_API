import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/chetan/PycharmProjects/Reqres_API/chromedriver")
driver.maximize_window()
driver.implicitly_wait(40)
driver.get('https://jqueryui.com/draggable/')
driver.switch_to.frame(0)
before = driver.get_window_position()
source1 = driver.find_element(By.ID, 'draggable')
action = ActionChains(driver)
action.drag_and_drop_by_offset(source1, 100, 100).perform()
time.sleep(5)
after = driver.get_window_position()

print('Before :',before)
print('After: ', after)
driver.get('https://jqueryui.com/droppable/')
driver.switch_to.frame(0)
source1 = driver.find_element(By.ID, 'draggable')
target1 = driver.find_element(By.ID, 'droppable')
actions2 = ActionChains(driver)
actions2.drag_and_drop(source1, target1).perform()
time.sleep(5)
if "Dropped!" == target1.text:
    print('Drag and drop is successfully')
    driver.close()
else:
    assert False
time.sleep(2)
