'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 16, 2025

Activity :
- Open URL Login page
-
'''

#importing the modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#initiate webdriver
driver = webdriver.Chrome()
driver.maximize_window()

def login_practice():
    # open url
    driver.get("https://practice.expandtesting.com/login")

    # locate username and password
    username = driver.find_element(By.XPATH, "//input[@id ='username']")
    password = driver.find_element(By.XPATH, "//input[@id ='password']")

    # send username and password
    username.send_keys("practice")
    password.send_keys("SuperSecretPassword!")

    # locate Login button
    # login_button = driver.find_element(By.XPATH,"//button[@id ='submit-login']")

    # locate login button using (contains) method
    # login_button = driver.find_element(By.XPATH, "//button[contains(@class,'btn-primary')]")

    # locate login button using text method
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")

    # click login button
    login_button.send_keys(Keys.RETURN)

    time.sleep(3)
    driver.quit()

def fb_forgot_password_page():
    driver.get("https://en-gb.facebook.com/")
    time.sleep(3)
    #locate link text by LINK_TEXT
    # forget = driver.find_element(By.LINK_TEXT, "Forgotten password?")

    # locate link text by PARTIALLINK_TEXT
    # forget = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten")
    # forget.click()

    #finding and clicking in same line
    driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten").click()

    #verify the page by title
    expected_title = "Forgotten Password | Can't Log In | Facebook"

    title = driver.title

    if title == expected_title:
        print(f"Test Passed")
    else:
        print(f"Test Failed, Got other title:{title}")

    time.sleep(3)
    driver.quit()

def fb_with_index_locators():
    driver.get("https://en-gb.facebook.com/")
    time.sleep(3)

    # finding and clicking in same line
    driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten").click()

    #locate username and password using index
    driver.find_element(By.XPATH,"(//input)[1]").send_keys("test_mail")
    driver.find_element(By.XPATH,"(//input)[2]").send_keys("test_passsword")



    time.sleep(3)
    driver.quit()

def Scroll_Practice():
    # open url
    driver.get("https://practice.expandtesting.com/login")

    # locate username and password
    username = driver.find_element(By.XPATH, "//input[@id ='username']")
    password = driver.find_element(By.XPATH, "//input[@id ='password']")
    time.sleep(3)
    #javascript to execute scroll till element
    driver.execute_script("arguments[0].scrollIntoView(true);",password)

    # send username and password
    username.send_keys("practice")
    password.send_keys("SuperSecretPassword!")

    # locate Login button
    # login_button = driver.find_element(By.XPATH,"//button[@id ='submit-login']")

    # locate login button using (contains) method
    # login_button = driver.find_element(By.XPATH, "//button[contains(@class,'btn-primary')]")

    # locate login button using text method
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    time.sleep(3)
    # javascript to execute scroll till element
    driver.execute_script("arguments[0].scrollIntoView(true);",login_button)
    # click login button
    login_button.send_keys(Keys.RETURN)

    time.sleep(3)
    driver.quit()



# login_practice()
# fb_forgot_password_page()
# fb_with_index_locators()
Scroll_Practice()

