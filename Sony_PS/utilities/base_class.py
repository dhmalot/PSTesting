import inspect

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import logging
from webdriver_manager.chrome import ChromeDriverManager


# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

# First way to create driver object
# service_Obj = Service("/home/user/drivers/chromedriver")
# driver = webdriver.Chrome(service=service_Obj)

# Second way to create driver object
# driver = webdriver.Chrome("/home/user/drivers/chromedriver")

# Third way to create driver object
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

@pytest.mark.usefixtures("setup")
class base_class:

    def wait_for_element_to_presence(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located(locator))

    def wait_for_element_to_be_visible(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of_element_located(locator))

    def select_dropdown_using_visible_text(self, text_value, element):
        dropdown = Select(element)
        dropdown.select_by_visible_text(text_value)

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
