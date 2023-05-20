import time

import pytest

from src.Pages.LoginPage import LoginPage
from src.test_cases.test_base import BaseTest

class Test_login(BaseTest):
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        time.sleep(5)
        self.loginPage.click_on_signin()
        time.sleep(10)
        print("sign printed")
        ## self.loginPage.click_create_new_account()
        self.loginPage.general_click(self.loginPage.create_new_account)
        time.sleep(10)
        ## self.loginPage.click_create()
        self.loginPage.general_click(self.loginPage.create_an_account)
        time.sleep(10)
        self.loginPage.select_value_from_dropdown(self.loginPage.country_region, "India")
        time.sleep(10)
        self.loginPage.general_click(self.loginPage.next_button)
        time.sleep(5)
        self.loginPage.select_value_from_dropdown(self.loginPage.month, "12")
        time.sleep(5)
        self.loginPage.select_value_from_dropdown(self.loginPage.day, "17")
        time.sleep(5)
        self.loginPage.select_value_from_dropdown(self.loginPage.year, "2002")
        time.sleep(5)
        self.loginPage.general_click(self.loginPage.next_button)
        time.sleep(7)
        self.loginPage.enter_mail("jeseeansari18@gmail.com")
        time.sleep(5)
        # self.loginPage.enter_credentials(self.loginPage.sign_in_id, "jeseeansari18@gmail.com")
        # time.sleep(5)
        self.loginPage.enter_password("Raroje@29")
        time.sleep(5)
        self.loginPage.re_enter_pw("Raroje@29")
        time.sleep(5)
        self.loginPage.general_click(self.loginPage.next_button)
        time.sleep(5)
        self.loginPage.enter_credentials(self.loginPage.city, "Mysore")
        time.sleep(5)
        self.loginPage.enter_credentials(self.loginPage.state, "Karnataka")
        time.sleep(3)
        self.loginPage.enter_credentials(self.loginPage.post_code, "570004")
        time.sleep(3)
        self.loginPage.general_click(self.loginPage.next_button)
        time.sleep(5)
        self.loginPage.enter_credentials(self.loginPage.online_id, "Takchia23")
        time.sleep(5)
        self.loginPage.enter_credentials(self.loginPage.first_name, "jesee")
        time.sleep(7)
        self.loginPage.enter_credentials(self.loginPage.last_name, "farht")
        time.sleep(5)
        self.loginPage.general_click(self.loginPage.next_button)
        time.sleep(5)
        self.loginPage.general_click(self.loginPage.receive_email)
        time.sleep(5)
        self.loginPage.general_click(self.loginPage.agree_continue)
        time.sleep(5)









