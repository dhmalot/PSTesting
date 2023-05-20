import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://id.sonyentertainmentnetwork.com/id/create_account_ca/?entry=create_account&auth_ver=v3&ui=pr&access_type=offline&client_id=e4a62faf-4b87-4fea-8565-caaabb3ac918&no_captcha=false&redirect_uri=https%3A%2F%2Fweb.np.playstation.com%2Fapi%2Fsession%2Fv1%2Fsession%3Fredirect_uri%3Dhttps%253A%252F%252Fio.playstation.com%252Fcentral%252Fauth%252Flogin%253Flocale%253Den_IN%2526postSignInURL%253Dhttps%25253A%25252F%25252Fwww.playstation.com%25252Fen-in%25252F%2526cancelURL%253Dhttps%25253A%25252F%25252Fwww.playstation.com%25252Fen-in%25252F%26x-psn-app-ver%3D%2540sie-ppr-web-session%252Fsession%252Fv5.28.0-uks.0&response_type=code&scope=web%3Acore&service_entity=urn%3Aservice-entity%3Apsn&smcid=web%3Apdc&state=d6245bf1366592b31688fe259acdb98d06024ff4ea5717f5d729603eb91a7cd2&cid=403c011d-67c0-4b4a-ac4c-01f2f7502c54&duid=0000000700090100cdbd589e7c9ecec22ad3732246aac4f1a30c6e67d43f7358dd79accc0b830e13#/create_account/wizard/agreement?entry=create_account")
driver.maximize_window()
driver.delete_all_cookies()
time.sleep(10)
driver.find_element(By.XPATH, "//button[@title = 'Checkbox Off']").click()
time.sleep(10)
# dropdown = driver.find_element(By.XPATH, "//select[@class='pulldown-text icon-pulldown-arrow']")
# sel = Select(dropdown)
# sel.select_by_visible_text("India")
# time.sleep(10)



