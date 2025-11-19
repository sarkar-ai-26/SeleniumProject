'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 19, 2025

Activity:
Learning waits
- Implicite wait
- Explicit wait

'''


from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



#create object of driver
driver = webdriver.Chrome()
driver.maximize_window()


def ImpliciteWait():
    # open demo url
    driver.get("https://www.saucedemo.com")

    #add IMPLICIT Wait
    driver.implicitly_wait(5) #--------------------- This Line ------------------------

    # Locate username using by.ID
    username = driver.find_element(By.ID, value="user-name")
    # Locate password using by.Name
    password = driver.find_element(By.NAME, value="password")
    # enter username
    username.send_keys("standard_user")
    # enter password
    password.send_keys("secret_sauce")
    # Find element by By.CLASS_NAME
    submit_button = driver.find_element(By.CLASS_NAME, value="btn_action")

    submit_button.click()
    # find element by link text
    product = driver.find_element(By.LINK_TEXT, value="Sauce Labs Backpack")
    product.click()

    # find element for addtocart with any locator
    add_to_cart = driver.find_element(By.ID, value="add-to-cart")

    add_to_cart.click()

    # find Element of cart by class name
    cart = driver.find_element(By.CLASS_NAME, value="shopping_cart_link")
    cart.click()


    # close browser
    driver.quit()

def ExplicitWait():
    # open demo url
    driver.get("https://www.saucedemo.com")

    #for explicit wait , creating object of wait with threashold of 10 sec
    wait = WebDriverWait(driver,10, ignored_exceptions= [NoSuchElementException,TimeoutError,Exception])

    # Locate username using by.ID using explicit wait

    username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))

    # Locate password using by.Name using explicit wait
    password = wait.until(EC.presence_of_element_located((By.ID,"password")))
    # password = wait.until(EC.((By.ID,"password")))
    # enter username
    username.send_keys("standard_user")
    # enter password
    password.send_keys("secret_sauce")
    # Find element by By.CLASS_NAME using explicit wait
    submit_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"btn_action")))
    submit_button.click()

    # find element by link text
    product = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Sauce Labs Backpack")))
    product.click()

    # find element for addtocart with any locator
    # add_to_cart = driver.find_element(By.ID, value="add-to-cart")
    add_to_cart = wait.until(EC.presence_of_element_located((By.ID,"add-to-cart")))
    add_to_cart.click()

    # find Element of cart by class name
    # cart = driver.find_element(By.CLASS_NAME, value="shopping_cart_link")
    cart = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
    cart.click()

    time.sleep(5)
    # close browser
    driver.quit()



# ImpliciteWait()
ExplicitWait()