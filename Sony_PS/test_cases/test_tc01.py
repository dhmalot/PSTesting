import time

from selenium.webdriver import Keys

import sys

sys.path.insert(0, "..")
from Sony_PS.utilities.base_class import base_class
from Sony_PS.Pages.GoogleSearchPage import GoogleSearch

# TestCases is class & it contains test cases. .
class TestCase_01(base_class):

    def test_testcase_01(self):
        google_search = GoogleSearch(self.driver)
        web_page_title = "Google"
        try:
            if self.driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(self.driver.title, web_page_title)
        except Exception as error:
            print(error)
        google_search.getSearchText().click()

        time.sleep(2)
        # google_search.getSearchText().send_keys(Keys.ENTER)
        google_search.getSubmit().send_keys("abhisisc@gmail.com")
        time.sleep(5)

        google_search.next_clicks().click()
        time.sleep(5)
        google_search.passwords().send_keys("Abhishek@07")
        time.sleep(5)
        # google_search.signin().click()
        # time.sleep(5)
        # google_search.signinlogo().click()
        # time.sleep(10)
        # google_search.signout().click()


        time.sleep(2)
        print(self.driver.title)
