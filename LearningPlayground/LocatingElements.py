'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 15, 2025

Activity:

Locating items using diffrent functions:
ByID, ByName, ByClassName, ByXPath

'''

#import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#create object of driver
driver = webdriver.Chrome()
driver.maximize_window()
#open demo url
driver.get("https://www.saucedemo.com")
time.sleep(1)

#Locate username using by.ID
username = driver.find_element(By.ID, value="user-name")

#Locate password using by.Name
password = driver.find_element(By.NAME, value="password")

#enter username
username.send_keys("standard_user")

#enter password
password.send_keys("secret_sauce")

#Find element and click Submit using By.ID
# submit_button = driver.find_element(By.ID, value = "login-button")

#Find element and click Submit using By.Xpath
# submit_button = driver.find_element(By.XPATH, value = "//input[@id='login-button']")

#Find element by By.CLASS_NAME
submit_button = driver.find_element(By.CLASS_NAME, value = "btn_action")

submit_button.click()

#find element by link text
product = driver.find_element(By.LINK_TEXT, value="Sauce Labs Backpack")

#find element by partial link text
# product = driver.find_element(By.PARTIAL_LINK_TEXT, value="Backpack")
product.click()
time.sleep(1)

#find element for addtocart with any locator
add_to_cart = driver.find_element(By.ID,value="add-to-cart")

#find element for add_to_cart with tagName
# add_to_cart = driver.find_element(By.TAG_NAME,value="button")

add_to_cart.click()

#find Element of cart by class name
cart = driver.find_element(By.CLASS_NAME, value = "shopping_cart_link")
cart.click()

time.sleep(5)

#close browser
driver.quit()

print("fffff")