import time

import pytest
from selenium.webdriver import Keys

import sys



sys.path.insert(0, "..")
from Sony_PS.utilities.base_class import base_class
from Sony_PS.Pages.GoogleSearchPage import GoogleSearch


class TestCase_02(base_class):
    # @pytest.mark.skip

    def test_testcase_04(self):
        google_search = GoogleSearch(self.driver)
        google_search.search_button().click()
        time.sleep(10)




    def test_testcase_03(self):
        google_search = GoogleSearch(self.driver)
        # web_page_title = "Google"
        v = google_search.get_text_of_header()
        print(v)

    def test_testcase_02(self):
        google_search = GoogleSearch(self.driver)
        # web_page_title = "Google"
        v = google_search.get_text_of_header()
        print(v)



















        time.sleep(2)
        print(self.driver.title)
