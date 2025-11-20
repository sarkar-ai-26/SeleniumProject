'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 20, 2025

Activity:
Learning working with:
- Basis Authentication PopUp

https://username:password@website.com
'''

#import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

def basicAuth(username,password):

    driver.get(f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth")
    time.sleep(4)
    print(f"Web page opened with basis authetication, username{username}, password{password}")
    if driver.title == "The Internet":
        print("Basic Auth Completed")

    tex = driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations! You must have the proper credentials.')]").text
    print(tex)

    time.sleep(2)
    driver.close()

username = "admin" 
password = "admin"
basicAuth(username,password)

