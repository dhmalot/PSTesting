import time

import pytest

from src.Pages.LoginPage import LoginPage
from test.test_base import BaseTest

class Test_Login_Page(BaseTest):

    def test_login_button(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.click_on_signin_button()

    @pytest.mark.xfail
    def test_do_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.click_on_signin_button()
        self.login_page.enter_email()
        time.sleep(10)
        self.login_page.click_on_next_button()
        time.sleep(10)
        self.login_page.enter_password()
        time.sleep(10)
        self.login_page.click_on_submit_button()
        time.sleep(20)


    def test_home_page_header(self):
        self.login_page = LoginPage(self.driver)
        elems = self.login_page.get_text_of_header()
        print(elems)






