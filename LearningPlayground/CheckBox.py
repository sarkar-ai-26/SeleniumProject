'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 1, 2025

Activity :
- CHeckBox
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

def SingleCheckBox():
    #open url
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    time.sleep(3)

    #get webpage title and verify
    if driver.title == "Different WebElements":
        print("On the webpage")

    #get web current url
    print(f"Current Page URL: {driver.current_url}")

    #get element for checkbox options

    option1 = driver.find_element(By.XPATH,"//input[@id='option1']")
    # verify selection
    if option1.is_selected():
        print("Already checked")
    else:
        option1.click()
        print("Checked")

    option2 = driver.find_element(By.XPATH, "//input[@id='option2']")
    # verify selection
    if option2.is_selected():
        print("Already checked")
    else:
        option2.click()
        print("Checked")

    option3 = driver.find_element(By.XPATH, "//input[@id='option3']")
    # verify selection
    if option3.is_selected():
        print("Already checked")
    else:
        option3.click()
        print("Checked")


    time.sleep(3)
    driver.close()


def MultipleCheckBox():
    #open url
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    time.sleep(3)

    #get webpage title and verify
    if driver.title == "Different WebElements":
        print("On the webpage")

    #get web current url
    print(f"Current Page URL: {driver.current_url}")

    #get element for checkbox options
    options = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    for option in options:
        print(option.text)
        if not option.is_selected():
            option.click()

    time.sleep(3)
    driver.close()


# SingleCheckBox()
MultipleCheckBox()