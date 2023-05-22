from selenium.webdriver.common.by import By


class GoogleSearch:
    # search_text = (By.XPATH, "//textarea[@name='q']")
    # submit_button = (By.XPATH, "(//input[@name='btnK' and @role='button'])[2]")
    # logo = (By.XPATH, "//img[@class='lnXdpd']")
    search_text = (By.XPATH, "// div[ @class ='psw-root psw-light-theme web-toolbar'] // span[@ class ='psw-fill-x psw-t-truncate-1 psw-l-space-x-2 ']")
    submit_button = (By.XPATH, "//input[@name='email']")
    # logo = (By.XPATH, "//img[@class='lnXdpd']")
    Next_bt = (By.XPATH, "//button[@class='primary-button row-button text-button']")
    password = (By.XPATH,"//input[@name='current-password']")
    sign_in= (By.XPATH,"//button[@id='signin-password-button']")
    sign_in_logo = (By.XPATH,"//span[@class='psw-media-frame psw-fill-x psw-image psw-icon-size-3 psw-r-pill psw-clip psw-aspect-1-1']")
    sign_out = (By.XPATH,"//span[text()= 'Sign Out']")

    header_nav_element = (By.CLASS_NAME, "shared-nav__primary-item")
    search_bt = (By.XPATH, "//button[@data-qa='shared-nav-search-button']")





    def __init__(self, driver):
        self.driver = driver

    def getSearchText(self):
        return self.driver.find_element(*GoogleSearch.search_text)

    def getSubmit(self):
        return self.driver.find_element(*GoogleSearch.submit_button)

    def next_clicks(self):
        return self.driver.find_element(*GoogleSearch.Next_bt)
    def passwords(self):
        return self.driver.find_element(*GoogleSearch.password)
    def signin(self):
        return self.driver.find_element(*GoogleSearch.sign_in)
    def signinlogo(self):
        return self.driver.find_element(*GoogleSearch.sign_in_logo)
    def signout(self):
        return self.driver.find_element(*GoogleSearch.sign_out)
    def search_button(self):
        return self.driver.find_element(*GoogleSearch.search_bt)
    def header_elemnts(self):
        return self.driver.find_element(*GoogleSearch.header_nav_element)

    def get_text_of_header(self):

        header_elements = []

        elements = self.driver.find_elements(*GoogleSearch.header_nav_element)
        for ele in elements:
            text = ele.text
            header_elements.append(text)

        return header_elements


