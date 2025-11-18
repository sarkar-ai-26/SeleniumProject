'''
Author : Yash Raj
GitHub : https://github.com/sarkar-ai-26
Created on Nov 16, 2025

Activity :
- Select class dropdown
'''

#importing the modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#initiate webdriver
driver = webdriver.Chrome()
driver.maximize_window()

def singleSelect_dp(option):
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    time.sleep(3)

    S_dropdown = driver.find_element(By.XPATH, "//select[@id='carBrands']")

    driver.execute_script("arguments[0].scrollIntoView(true);", S_dropdown)
    time.sleep(3)
    select = Select(S_dropdown)

    # select.select_by_value(option)
    # select.select_by_index(0)
    # select.select_by_visible_text(option)

    list_options = select.options
    print(len(list_options))
    for item in list_options:
        print(item.text)
        if item.text == option:
            print("ff")
            item.click()
            break

    time.sleep(5)

    driver.close()


def MultiSelect_dp():
    driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
    time.sleep(3)

    m_dropdown = driver.find_element(By.ID, "multiSelect")

    driver.execute_script("arguments[0].scrollIntoView(true);", m_dropdown)
    time.sleep(3)
    select = Select(m_dropdown)

    select.select_by_visible_text("Mercedes")
    select.select_by_visible_text("Saab")
    select.select_by_visible_text("Audi")

    #deselect the item
    select.deselect_by_visible_text("Mercedes")

    select.deselect_all()

    # select.select_by_index(0)
    # select.select_by_visible_text(option)

    # list_options = select.options
    # print(len(list_options))
    # for item in list_options:
    #     print(item.text)
    #     if item.text == option:
    #         item.click()
    #         break

    time.sleep(5)

    driver.close()


# option = "Mercedes"
# singleSelect_dp(option)
MultiSelect_dp()