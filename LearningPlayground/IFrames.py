'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 20, 2025

Activity:
Learning working with:
- Frames
- IFrames

Practice webpage is in
SeleniumPython\iframePracticeSite
- index.html
'''

#import required modules

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

def iFrame():
    driver.get("C:\YashAssets\PythonProjects\Selenium\SeleniumProject\iframePracticeSite\index.html")
    wait = WebDriverWait(driver,10)
    #switch to left frame
    driver.switch_to.frame("leftFrame")
    print("Frame switched to leftFrame")

    name = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='name']")))
    name.send_keys("Sarkar")
    print("Name filled")

    email = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='email']")))
    email.send_keys("sarkar@gmail.com")
    print("Email filled")

    submit_bt = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='submit']")))
    submit_bt.click()
    print("Button Clicked")

    time.sleep(4)

    #switch to default content
    driver.switch_to.default_content()
    print("Switch to default content frame")

    #swithc to right frame
    # driver.switch_to.frame("rightFrame")

    #Switching via element
    rightframe = driver.find_element(By.XPATH, "//iframe[@name='rightFrame']")
    driver.switch_to.frame(rightframe)
    print("Switched to Right frame")


    click_me = wait.until(EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'Click Me')]")))
    click_me.click()
    print("Clicked on click me")

    time.sleep(2)

    al = driver.switch_to.alert
    al.accept()
    print("Alert accepted")
    time.sleep(2)
    option = driver.find_element(By.XPATH,"//select[@id='options']")

    sl = Select(option)

    sl.select_by_visible_text("Option Two")
    print("Option two selected from dropdown")

    time.sleep(3)

    driver.switch_to.default_content() #switching to deafult content
    print("Switched to default content")

    driver.switch_to.frame("bottomFrame")

    bt_text = driver.find_element(By.TAG_NAME, "p").text
    print(f"Botton text: {bt_text}")


    driver.close()

def nestedFrame():

    driver.get("file:///C:/YashAssets/PythonProjects/Selenium/SeleniumProject/iframePracticeSite/nested-frame.html")

    driver.switch_to.frame("parentFrame")

    p_t = driver.find_element(By.TAG_NAME,"h3").text
    p_tt = driver.find_element(By.TAG_NAME, "p").text
    print(p_t)
    print(p_tt)

    time.sleep(3)

    driver.switch_to.frame("childFrame")
    c_t = driver.find_element(By.TAG_NAME, "h4").text
    c_tt = driver.find_element(By.TAG_NAME, "p").text
    print(c_t)
    print(c_tt)


def ExplicitWaitiFrame():

    driver.get("file:///C:/YashAssets/PythonProjects/Selenium/SeleniumProject/iframePracticeSite/nested-frame.html")
    wait = WebDriverWait(driver,10)
    p_frames = driver.find_elements(By.NAME,"parentFrame")
    #check if frame is not empty
    if p_frames:
        try:
            # driver.switch_to.frame("parentFrame")
            wait.until(EC.frame_to_be_available_and_switch_to_it
                       ((By.NAME, "parentFrame")))
            p_t = driver.find_element(By.TAG_NAME, "h3").text
            p_tt = driver.find_element(By.TAG_NAME, "p").text
            print(p_t)
            print(p_tt)

            # driver.switch_to.frame("childFrame")
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME,"childFrame")))
            c_t = driver.find_element(By.TAG_NAME, "h4").text
            c_tt = driver.find_element(By.TAG_NAME, "p").text
            print(c_t)
            print(c_tt)

        except Exception as e:
            print("Frame error : ", e)
    else:
        print("Parent frame is empty")



    time.sleep(3)


# iFrame()
# nestedFrame()