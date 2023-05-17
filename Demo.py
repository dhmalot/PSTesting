import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= r"C:\Users\7000033861\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.airindia.com/?utm_source=google&utm_medium=cpc&utm_campaign=brand-exact&gad=1&gclid=EAIaIQobChMI7ceVsIj8_gIVW5hmAh0C8QO7EAAYASAAEgJU1vD_BwE")
driver.maximize_window()
driver.delete_all_cookies()
driver.find_element(By.XPATH, "//img[@title = 'Air India Logo']").click()
time.sleep(10)
#landingpage_title = driver.title
#print(landingpage_title)
# elements = driver.find_elements(By.XPATH,"//div[@class='shared-nav__secondary-parent shared-nav__secondary-parent--msg_games']//section[@aria-label='Dropdown Menu']/div[@class='shared-nav__secondary-item']")
# games_category_elements = []
# for ele in elements:
#     text = ele.text
#     games_category_elements.append(text)
# print(games_category_elements)
#