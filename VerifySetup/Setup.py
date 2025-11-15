'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 13, 2025

Activity:
Verify Selenium setup, chrome launch

'''

#import webdriver module drom selenium package
from selenium import webdriver
#initiate object of webdriver to launch chrome
driver = webdriver.Chrome()
#open an url
driver.get("https://www.google.com")

driver.quit()