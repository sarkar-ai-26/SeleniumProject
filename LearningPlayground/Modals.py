'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 18, 2025

Activity :
- Handling Modals
- Modals are webpage alerts for alerting something, or filling forms.
'''

#import the required modules

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#create object to start browser window
driver = webdriver.Chrome()
#maximize window
driver.maximize_window()

def AlertModal():
    driver.get("https://practice-automation.com/modals/")

    #click simple modal button
    driver.find_element(By.XPATH, "//button[@id='simpleModal']").click()
    print(f"Button clicked")
    #click the cross button to close the modal popup
    time.sleep(3)

    text = driver.find_element(By.XPATH, "(//div[@class='pum-content popmake-content']/p)[1]")
    print(f"Mesage: {text.text}")

    driver.find_element(By.XPATH,"(//button[@class='pum-close popmake-close'])[1]").click
    print(f"Pop up closed")
    driver.close()


def FormvModal():
    driver.get("https://practice-automation.com/modals/")

    #click simple modal button
    driver.find_element(By.XPATH, "//button[@id='formModal']").click()
    print(f"Button clicked")
    #click the cross button to close the modal popup
    time.sleep(3)
    # driver.find_element(By.XPATH,"(//button[@class='pum-close popmake-close'])[2]").click
    # print(f"Pop up closed")

    #filling modal form
    name = driver.find_element(By.XPATH, "//input[@id='g1051-name']")
    name.send_keys("TestName"
                   )
    email = driver.find_element(By.XPATH, "//input[@id='g1051-email']")
    email.send_keys("testemail@gmail.com")

    submit_button = driver.find_element(By.XPATH,"(//button[@type='submit'])[2]")
    time.sleep(3)
    driver.execute_script("arguments[0].scrollIntoView(true);",submit_button)

    time.sleep(3)
    submit_button.click()

    driver.close()

AlertModal()
# FormvModal()