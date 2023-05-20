import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class basepage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, bylocator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(bylocator)).click()

    def send_text(self, bylocator, text):
        keys = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(bylocator))
        keys.send_keys(text)
        time.sleep(10)

