import time

from selenium.webdriver.common.by import By
# from basepage import basepage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys

from src.Pages.basepage import basepage


class LoginPage(basepage):
    # email = (By.XPATH, "//input[@name ='email']")
    # next_button = (By.XPATH, "//button[@type ='submit']")
    # password = (By.XPATH, "//input[@name ='current-password']")
    sign_in = (By.XPATH, "/span[text() = 'Sign In']")
    create_new_account = (By.XPATH, "//button[@class='secondary-button row-button text-button']")
    create_an_account = (By.XPATH, "//button[@class='primary-button row-button text-button']")
    country_region = (By.XPATH, "//select[@class='pulldown-text icon-pulldown-arrow']")
    next_button = (By.XPATH, "//button[@class='next-button text-button']")
    month = (By.XPATH, "//select[@title = 'Month']")
    day = (By.XPATH, "//select[@title='Day']")
    year = (By.XPATH, "//select[@title='Year']")
    sign_in_id = (By.XPATH, "//input[@title = 'Email Address']")
    password = (By.XPATH, "//input[@name = 'new-password']")
    re_enter_password = (By.XPATH, "//input[@title = 'Re-enter Password']")

    next_button_1 = (By.XPATH, "//button[@class='next-button text-button']")
    next_button_2 = (By.XPATH, "//button[@class='next-button text-button']")
    parental_next = (By.XPATH, "//button[@class='primary-button row-button text-button']")
    sign_in_last = (By.XPATH, "//button[@class='primary-button row-button text-button']")
    city = (By.XPATH, "//input[@title = 'City']")
    state = (By.XPATH, "//input[@title = 'State or Province']")
    post_code = (By.XPATH, "//input[@title = 'Postcode']")
    online_id = (By.XPATH, "//input[@title = 'Online ID']")
    first_name = (By.XPATH, "//input[@title = 'First Name']")
    last_name = (By.XPATH, "//input[@title = 'Last Name']")
    receive_email = (By.XPATH, "//button[@title = 'Checkbox Off']")
    agree_continue = (By.XPATH, "//button[@class = 'primary-button row-button text-button']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.playstation.com/en-in/")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

    def click_on_signin(self):
        # self.click_on_element(self.sign_in)
        self.driver.find_element(By.XPATH, "//span[text() = 'Sign In']").click()

    def click_create_new_account(self):
        self.click_on_element(self.create_new_account)

    def click_create(self):
        self.click_on_element(self.create_an_account)

    def general_click(self, locator):
        self.click_on_element(locator)



    def select_value_from_dropdown(self, locator: str, value):
        # Select select = new Select(driver.findElement(By.id("oldSelectMenu")));
        # x = self.driver.find_element_by_id(locator)
        dd = self.driver.find_element(*locator)
        time.sleep(5)
        sel = Select(dd)
        sel.select_by_visible_text(value)
        time.sleep(10)

    def enter_credentials(self, value: str, creds):
        self.send_text(value, creds)

    def enter_mail(self, mail):
        self.driver.find_element(*self.sign_in_id).send_keys(mail)
        time.sleep(3)
        # sk.send_keys(mail)

    def enter_password(self, pw):
        self.driver.find_element(*self.password).send_keys(pw)
        time.sleep(3)

    def re_enter_pw(self, rpw):
        self.driver.find_element(*self.re_enter_password).send_keys(rpw)
        time.sleep(3)














