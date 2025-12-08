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
import os

driver = webdriver.Chrome()
driver.maximize_window()

def takeScreenshot():

    folder = r"C:\YashAssets\PythonProjects\Selenium\SeleniumProject\ScreenShots"

    if not os.path.exists(folder):
        os.mkdir(folder)

    driver.get("https://practice.expandtesting.com/tooltips")