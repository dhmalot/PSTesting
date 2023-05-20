import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

# from test_sample import chrome_options


@pytest.fixture(params = ['chrome'], scope='class')
def set_up(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--ignore-ssl-errors")
        # web_driver = webdriver.Chrome(executable_path= r"C:\Users\7000033861\Downloads\chromedriver_win32\chromedriver.exe")
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        request.cls.driver = web_driver
        yield
        web_driver.close()