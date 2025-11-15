'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 15, 2025

Activity:

Locating items using diffrent functions:
ByID, ByName, ByClassName, ByXPath

'''

#import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#create object of driver
driver = webdriver.Chrome()
driver.maximize_window()
#open demo url
driver.get("https://www.saucedemo.com")
time.sleep(3)

#Locate username using by.ID
username = driver.find_element(By.ID, value="user-name")

#Locate password using by.Name
password = driver.find_element(By.NAME, value="password")

#enter username
username.send_keys("standard_user")
time.sleep(3)

#enter password
password.send_keys("secret_sauce")
time.sleep(3)

#Find element and click Submit using By.ID
# submit_button = driver.find_element(By.ID, value = "login-button")

#Find element and click Submit using By.Xpath
submit_button = driver.find_element(By.XPATH, value = "//input[@id='login-button']")
submit_button.click()
time.sleep(5)

#close browser
driver.quit()