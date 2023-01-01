import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_run_script():
    driver = webdriver.Chrome(executable_path="/home/chetan/PycharmProjects/Reqres_API/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(40)
    driver.get('https://amazon.in')
    time.sleep(6)
    driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div[13]/div[2]/a/span").click()
    driver.find_element(By.ID, "ap_email").send_keys('+919154937900')
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "ap_password").send_keys('Vampire145@@')
    driver.find_element(By.ID, "signInSubmit").click()
    time.sleep(15)
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys('Wireless mouse')
    driver.find_element(By.ID, "nav-search-submit-button").click()
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div["
                        "3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img").click()
    time.sleep(2)


def test_login_script():
    driver = webdriver.Chrome(executable_path="/home/chetan/PycharmProjects/Reqres_API/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(40)
    driver.get('https://cqube-release.tibilprojects.com/#/login')
    time.sleep(2)
    driver.find_element(By.ID, "username1").send_keys('Admin')
    driver.find_element(By.ID, "password1").send_keys('Admin@123')
    time.sleep(1)
    driver.find_element(By.ID, "login").click()
    time.sleep(3)
    if 'home' in driver.current_url:
        print("Login is successfull ")
    else:
        print("Login is not working ")
        assert False
