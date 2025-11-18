'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 16, 2025

Activity :
- Handling Alerts
'''

#import the required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

def AcceptAlert():
    #launch wehpage
    driver.get("https://demo.guru99.com/V4/")

    #locating login button
    login_button = driver.find_element(By.XPATH,"//input[@name='btnLogin']")
    login_button.click() #click button

    #Switch focus to alert
    a = driver.switch_to.alert
    time.sleep(3)
    print(f"Alert message : {a.text}") # it will print the alert text message
    a.accept() # it will click on Accept or Ok alert

    time.sleep(4) #sleep to check behavior

    driver.close() #close browser


def AllAlerts():
    #launch weburl
    driver.get("http://uitestingplayground.com/alerts")

    accept_alert = driver.find_element(By.XPATH, "//button[@id='alertButton']") # locating alert button
    accept_alert.click() #click the button

    al = driver.switch_to.alert #change driver focus to alerts
    time.sleep(2)
    print(f"Alert message: {al.text}")
    al.accept() #accepts the alert

    time.sleep(3)

    confirm_alert = driver.find_element(By.XPATH,"//button[@id='confirmButton']") #locarting confirm alert
    confirm_alert.click() #click the button

    ca = driver.switch_to.alert # switch driver focus to confirm alert
    time.sleep(1)
    print(f"Confirm alert message : {ca.text}")
    # ca.accept() #accept the alert
    ca.dismiss() #reject/cancel the alert

    time.sleep(2)
    caa = driver.switch_to.alert #switch driver focus to yes alert
    caa.accept() #accept the alert

    time.sleep(3)

    prompt_alert = driver.find_element(By.XPATH, "//button[@id='promptButton']") #locate prompt button
    prompt_alert.click() #click the button
    time.sleep(2)

    pa = driver.switch_to.alert #switch driver focus to alerts
    print(f"Alert message: {pa.text}")
    pa.send_keys("dogs")
    time.sleep(2)
    pa.accept()
    time.sleep(2)
    paa = driver.switch_to.alert #switch driver focus to javascript alerts
    # paa.accept() #accpet the alert
    paa.dismiss() #accpet the alert

    time.sleep(4)
    driver.close()

# AcceptAlert()
AllAlerts()

