from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, bylocator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(bylocator)).click()

    def send_text(self, bylocator, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(bylocator)).send_keys(text)

    def get_text(self, bylocator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(bylocator))
        return element.text

    def get_title(self):
        return self.driver.title

