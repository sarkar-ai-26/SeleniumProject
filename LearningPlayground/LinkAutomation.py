'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 20, 2025

Activity:
Learning working with links
- Internal links
- External links
- Broken Links
'''

#import required libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

driver = webdriver.Chrome()
driver.maximize_window()

def linkAuto():
    driver.get("https://practice.expandtesting.com/")
    print("Web launched")
    wait = WebDriverWait(driver,10)
    page = wait.until(EC.presence_of_element_located((By.XPATH,"//a[contains(text(),'Test Login Page')]")))
    print("Element located")
    driver.execute_script("arguments[0].scrollIntoView(true);", page)
    print("Scrolled to element location")
    time.sleep(2)
    page.click()
    print("Clicked test login page")

    time.sleep(4)


def validbrokenLink():
    # driver.get("https://practice.expandtesting.com/")
    driver.get("https://demo.guru99.com/V4/")
    print("Webpage launched")

    wait = WebDriverWait(driver,10)

    links_list = driver.find_elements(By.TAG_NAME,"a")
    print(f"Total links: {len(links_list)}")
    valid_count = 0
    broken_count = 0
    #loop through all links to send request
    for link in links_list:

        url = link.get_attribute("href") #storing in url variable

        #make http head request to url
        try:
            response = requests.head(url,timeout=10)

            if response.status_code >= 400:
                print(f"Link Broken: {link.get_attribute("href")}")
                broken_count += 1
            else:
                print(f"Link Valid: {link.get_attribute("href")}")
                valid_count += 1

        except Exception as e:
            print("Error",e)

    driver.close()

    print(f"Valid Links : {valid_count}, Broken Links : {broken_count}")

# linkAuto()
validbrokenLink()