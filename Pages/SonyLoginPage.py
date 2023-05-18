from selenium.webdriver.common.by import By


class SonyLoginPage:
    search_button = (By.XPATH, "//button[@data-qa='shared-nav-search-button']")
    search_box = (By.XPATH, "//input[@data-qa='search-text-box']")
    search_box_search_button = (By.XPATH, "//button[contains(@class, 'search-button')]")

    def __init__(self, driver):
        self.driver = driver

    def get_search_button(self):
        return self.driver.find_element(*SonyLoginPage.search_button)

    def get_search_box(self):
        return self.driver.find_element(*SonyLoginPage.search_box)

    def get_search_box_button(self):
        return self.driver.find_element(*SonyLoginPage.search_box_search_button)
