import inspect

import pytest
import logging
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def wait_for_element_to_present(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located(locator))

    def wait_for_element_to_be_visible(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.visibility_of_element_located(locator))

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
