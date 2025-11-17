'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 16, 2025

Activity :
- Custom dropdown
- Custom searchable dropdown
'''

#importing the modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#initiate webdriver
driver = webdriver.Chrome()
driver.maximize_window()

def custom_dp(option):
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    time.sleep(3)

    c_dropdown = driver.find_element(By.XPATH, "//div[@id='custom-select']")

    driver.execute_script("arguments[0].scrollIntoView(true);", c_dropdown)
    time.sleep(3)
    c_dropdown.click()



    option_element = driver.find_element(By.XPATH, f"//div[@class ='custom-options']/div[text()='{option}']")
    option_element.click()

    time.sleep(3)

    driver.close()


def search_dp(option):
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    time.sleep(3)

    c_dropdown = driver.find_element(By.XPATH, "//div[@id='custom-select']")

    driver.execute_script("arguments[0].scrollIntoView(true);", c_dropdown)
    time.sleep(3)

    option_element = driver.find_element(By.XPATH, f"//input[@class='search-box']")
    option_element.send_keys(option)
    driver.find_element(By.XPATH,"//div[@class ='searchable-options']/div[text()='SUV']").click()

    time.sleep(3)

    driver.close()

# option = "Red"
option = "S"
# custom_dp(option)
search_dp(option)