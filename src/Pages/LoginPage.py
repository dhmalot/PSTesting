from src.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    #By locators

    SIGNIN = (By.XPATH, "//span[text() = 'Sign In']")
    EMAIL = (By.XPATH, "//input[@name = 'email']")
    NEXT = (By.XPATH, "//button[@type = 'submit']")
    PASSWORD = (By.XPATH, "//input[@type = 'password']")
    SUBMIT = (By.ID, "signin-password-button")
    HEADER = (By.CLASS_NAME, "shared-nav__primary-item")

    #constructor to call the driver and launch Playstation website

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.playstation.com/en-in/")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()


    # User Actions are created using the below methods

    def click_on_signin_button(self):
        self.click_on_element(self.SIGNIN)

    def enter_email(self):
        self.send_text(self.EMAIL, 'abhisisc@gmail.com')

    def click_on_next_button(self):
        self.click_on_element(self.NEXT)

    def enter_password(self):
        self.send_text(self.PASSWORD, 'Abhishek@07')

    def click_on_submit_button(self):
        self.click_on_element(self.SUBMIT)

    def get_text_of_header(self):
        header_elements = []
        elements = self.driver.find_elements(*LoginPage.HEADER)
        for ele in elements:
            text = ele.text
            header_elements.append(text)

        return header_elements



