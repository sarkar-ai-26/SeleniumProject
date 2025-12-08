'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Dec 8, 2025

Activity:
Learning working with tooltip:

- Mouse hover
- Drag and drop
- Double click
- Right Click
- Holding the keyboard keys
- Click and hold and release


'''

#import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

def toolKit():

    driver.get("https://practice.expandtesting.com/tooltips")
    title = driver.title
    print(title)
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver,10)

    actions = ActionChains(driver) #object of action chains

    #locate tooltip button
    # button1 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='btn1']")))
    button1 = driver.find_element(By.XPATH,"//button[@id='btn1']")
    actions.move_to_element(button1).perform()

    time.sleep(3)

    button1text = button1.get_attribute("title")
    print(f"button1text : {button1text}")

    driver.close()

toolKit()
