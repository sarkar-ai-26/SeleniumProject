'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 15, 2025

Activity:
Finding Multiple Elements and Handling them
Via ID, NAME, CLASS, TAGANAME, XPATH

Activity :
- Open URL Login page
- Find all input fields (username and password) with find_elements()
- Check if they exists
- Enter login details
- Click the login button

'''

#Import all the necessary modules

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Create driver object to launch browser
driver = webdriver.Chrome()

#Maximize the browser
driver.maximize_window()

#launch web url
driver.get("https://www.saucedemo.com")
time.sleep(2)

#Locate all input elements
inputs = driver.find_elements(By.TAG_NAME, "input")
print(len(inputs))

for i in range(0,len(inputs)):
    print(inputs[i].get_attribute("id"))

inputs[0].send_keys("standard_user")
inputs[1].send_keys("secret_sauce")
inputs[2].send_keys(Keys.RETURN)

product_list = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name ']")

#Fetch all the products on the inventory
for item in product_list:
    print(item.text)

time.sleep(3)

driver.quit()
