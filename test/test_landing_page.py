import time

from src.Config.config import TestData

from src.Pages.LandingPage import LandingPage
from test.test_base import BaseTest


class Test_Landing_Page(BaseTest):

    def test_tc01_the_games_category_products(self):
        self.landing_page = LandingPage(self.driver)
        self.landing_page.click_on_games()
        time.sleep(10)
        actual_list = self.landing_page.get_text_of_elements_in_games()
        print(actual_list)
        assert actual_list == TestData.LIST_OF_ELEMENTS_IN_GAMES_DROPDOWN

    def test_tc02_title_of_PS5(self):
        self.landing_page = LandingPage(self.driver)
        self.landing_page.click_on_games()
        self.landing_page.click_on_PS5()
        time.sleep(10)
        actual_title = self.landing_page.get_title()
        time.sleep(10)
        print(actual_title)
        assert actual_title == TestData.PS5_TITLE

    def test_tc03_title_of_PS4(self):
        self.landing_page = LandingPage(self.driver)
        self.landing_page.click_on_games()
        self.landing_page.click_on_PS4()
        time.sleep(10)
        actual_title = self.landing_page.get_title()
        time.sleep(10)
        print(actual_title)
        assert actual_title == TestData.PS4_TITLE

    def test_tc04_title_of_PS_VR2(self):
        self.landing_page = LandingPage(self.driver)
        self.landing_page.click_on_games()
        self.landing_page.click_on_PS_VR2()
        time.sleep(5)
        actual_title = self.landing_page.get_title()
        print(actual_title)
        assert actual_title == TestData.PS_VR2_TITLE

    def test_tc05_title_of_PS_Plus(self):
        self.landing_page = LandingPage(self.driver)
        self.landing_page.click_on_games()
        self.landing_page.click_on_PS_Plus()
        time.sleep(5)
        actual_title = self.landing_page.get_title()
        print(actual_title)
        assert actual_title == TestData.PS_PLUS_TITLE



