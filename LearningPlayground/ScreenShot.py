'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Dec 8, 2025

Activity:
Learning working with Screenshots

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

driver = webdriver.Chrome()
driver.maximize_window()

def takeScreenshot():

    folder = r"C:\YashAssets\PythonProjects\Selenium\SeleniumProject\ScreenShots"

    if not os.path.exists(folder):
        os.mkdir(folder)


    driver.get("https://practice.expandtesting.com/tooltips")

    file_path = folder + "//file_2.png"

    #full page screenshot
    # driver.get_screenshot_as_file(file_path)
    driver.save_screenshot(file_path)

    #element screenshot
    element_path = folder + "//elementfile.png"
    button1 = driver.find_element(By.XPATH, "(//div[@id='main-navbar']/ul/li)[2]")
    time.sleep(3)
    button1.screenshot(element_path)
    driver.close()

takeScreenshot()
