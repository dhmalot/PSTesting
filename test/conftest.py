import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params = ['chrome'], scope='class')
def set_up(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        web_driver = webdriver.Chrome(executable_path= r"C:\Users\7000033861\Downloads\chromedriver_win32\chromedriver.exe")
        request.cls.driver = web_driver
        yield
        web_driver.close()