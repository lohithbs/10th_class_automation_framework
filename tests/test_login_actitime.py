import time

from selenium import webdriver
import os


def test_setup():
    global driver
    driver_path=(os.getcwd().replace("tests","").replace("\\","/")+"drivers/"+"chromedriver.exe")
    driver=webdriver.Chrome(executable_path=driver_path)
    driver.get("http://localhost/login.do")
    driver.maximize_window()
    driver.implicitly_wait(10)

def test_login():
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_id("loginButton").click()
def test_logout():
    driver.find_element_by_class_name("logout").click()
    time.sleep(5)
    driver.quit()
test_setup()
test_login()
test_logout()
