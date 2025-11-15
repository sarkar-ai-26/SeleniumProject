'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 15, 2025

Activity:
Automate:
    1. Login Page
    2. Add Item to Cart
    3. Close browser

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

#Find element by By.CLASS_NAME
submit_button = driver.find_element(By.CLASS_NAME, value = "btn_action")

submit_button.click()

#find element by link text
product = driver.find_element(By.LINK_TEXT, value="Sauce Labs Backpack")

product.click()
time.sleep(1)

#find element for addtocart with any locator
add_to_cart = driver.find_element(By.ID,value="add-to-cart")

add_to_cart.click()

#find Element of cart by class name
cart = driver.find_element(By.CLASS_NAME, value = "shopping_cart_link")
cart.click()

time.sleep(5)

#close browser
driver.quit()