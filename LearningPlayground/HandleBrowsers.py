'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 20, 2025

Activity:
Learning working with:
- handle Browser
- Switch browser
- Switch Tab
- Close
- Quit

task:
1. Launch Browser
2. Open Target URL
3. Get the current window handle
4. Click link to open new window
5. fetch all windows id
6. Switch to new Window
7. Verify the window by checking title or URL
8. Perform actions in the new window
9. Close specific window, if needed
10. Switch back to original window
'''


#impport required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver =  webdriver.Chrome()
driver.maximize_window()

def WindowHandling():
    driver.get("https://the-internet.herokuapp.com/windows")
    print("Browser launched with URL")

    #Get the Unique ID of the currently active browser
    c_id = driver.current_window_handle
    print(f"Current Unique id: {c_id}")

    driver.find_element(By.LINK_TEXT,"Click Here").click()

    # Get the Unique ID of the new currently active browser
    new_c_id = driver.current_window_handle
    print(f"New page Uniquie id: {new_c_id}")

    # Get the Unique ID of all active browser
    all_id = driver.window_handles
    print(f"List of Unique iD of all active windows: {all_id}")

    #Switch focus to new window to interact
    for id in all_id:
        if id != c_id:
            driver.switch_to.window(id) #module to switch to window
            print(f"Switched to new window: {id}")

    #verify the switch window by title
    tt = driver.title

    if tt == "New Window":
        print("Switched window verified")
    else:
        print("Failed")

    text_on_web = driver.find_element(By.TAG_NAME,"h3").text
    print(text_on_web)

    time.sleep(5)
    driver.quit()


WindowHandling()