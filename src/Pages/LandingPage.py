from selenium.webdriver.common.by import By

from src.Config.config import TestData
from src.Pages.BasePage import BasePage


class LandingPage(BasePage):

    #landing page locators
    GAMES = (By.ID, "menu-button-primary--msg-games")
    ALL_ELEMENTS_IN_GAMES = (By.XPATH, "//div[@class='shared-nav__secondary-parent shared-nav__secondary-parent--msg_games']"
                                       "//section[@aria-label='Dropdown Menu']/div[@class='shared-nav__secondary-item']")
    PS5 = (By.XPATH, "//a[@id = 'link-secondary--msg-ps5']//span[text() = 'PS5']")
    PS4 = (By.XPATH, "//a[@id = 'link-secondary--msg-ps4']//span[text() = 'PS4']")
    PS_VR2 = (By.XPATH, "//a[@id = 'link-secondary--msg-ps-vr2']//span[text() = 'PS VR2']")
    PS_Plus = (By.XPATH,"//a[@id = 'link-secondary--msg-ps-plus']//span[text() = 'PS Plus']")

    HARDWARE = (By.ID, "menu-button-primary--msg-hardware")
    SERVICES = (By.ID, "menu-button-primary--msg-services")
    NEWS = (By.ID, "menu-button-primary--msg-news")
    SHOP = (By.ID, "menu-button-primary--msg-shop")
    SUPPORT = (By.ID, "menu-button-primary--msg-support")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.SONY_PLAYSTATION_LINK)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

    def click_on_games(self):
        self.click_on_element(self.GAMES)

    def get_text_of_elements_in_games(self):
        games_accessories_list = []
        elements = self.driver.find_elements(*LandingPage.ALL_ELEMENTS_IN_GAMES)
        for ele in elements:
            text = ele.text
            games_accessories_list.append(text)

        return games_accessories_list

    def click_on_PS5(self):
        self.click_on_element(self.PS5)

    def click_on_PS4(self):
        self.click_on_element(self.PS4)

    def click_on_PS_VR2(self):
        self.click_on_element(self.PS_VR2)

    def click_on_PS_Plus(self):
        self.click_on_element(self.PS_Plus)


################################################################################
    def click_on_hardware(self):
        self.click_on_element(self.HARDWARE)

    def click_on_services(self):
        self.click_on_element(self.SERVICES)

    def click_on_news(self):
        self.click_on_element(self.NEWS)

    def click_on_shop(self):
        self.click_on_element(self.SHOP)

    def click_on_support(self):
        self.click_on_element(self.SUPPORT)

