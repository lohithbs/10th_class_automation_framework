from selenium import webdriver
import os
driver_path=(os.getcwd().replace("tests","").replace("\\","/")+"drivers/"+"chromedriver.exe")
driver=webdriver.Chrome(executable_path=driver_path)
