'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 18, 2025

Activity :
- Dynamic searchable dropdown
'''

#importing the modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#initiate webdriver
driver = webdriver.Chrome()
driver.maximize_window()


def dynamic_search_dp(option):
    driver.get("https://www.google.com/")
    time.sleep(3)

    dropdown = driver.find_element(By.XPATH, "//textarea[@title='Search']")

    dropdown.send_keys(option)
    time.sleep(4)

    list_option = driver.find_elements(By.XPATH,"//ul[@role='listbox']//li")
    for option in list_option:
        print(option.text)

    time.sleep(3)

    driver.close()


option = "Car"
dynamic_search_dp(option)