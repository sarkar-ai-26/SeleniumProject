'''
Author : Yash Raj
Created on Nov 14, 2025

Activity:
a) Opening web page
b) Navigating web page
    - Navigate to Google
    - Navigate to youtube
    - go back to Google
    - go forward to YouTube
    - Refresh the current page (Youtube)
    - Navigate to Google
    - Close the brower
    
'''

#import webdriver module
from selenium import webdriver
import time

#create object of webdriver to launch driver
driver = webdriver.Chrome()
#maximize browser
driver.maximize_window()

google_url = "https://www.google.com"
youtube_url = "https://www.youtube.com"

#Navigate to Google
driver.get(google_url)
time.sleep(3)

#Navigate to youtube
driver.get(youtube_url)
time.sleep(3)

#go back to Google
driver.back()

#go forward to YouTube
driver.forward()

#Refresh the current page (Youtube)
driver.refresh()
time.sleep(3)

#Navigate to Google
driver.back()
time.sleep(3)

#Close the brower
driver.quit()
#done

