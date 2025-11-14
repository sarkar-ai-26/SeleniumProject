#import webdriver module drom selenium package
from selenium import webdriver
#initiate object of webdriver to launch chrome
driver = webdriver.Chrome()
#open an url
driver.get("https://www.google.com")

driver.quit()