'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 1, 2025

Activity :
- RadioButtons (Only one should be select out of all buttons )
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

def RadioButton():
    #open url
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='radio2']").click()
    print("Clicked Radio Button 2")

    driver.find_element(By.XPATH, "//input[@id='radio3']").click()
    print("Clicked Radio Button 3")

    button = driver.find_element(By.XPATH, "//input[@id='radio4']")
    button.click()
    print("Clicked Radio Button 4")

    print(f"Radio button 4 selected : {button.is_selected()} ")
    time.sleep(3)
    driver.close()

RadioButton()