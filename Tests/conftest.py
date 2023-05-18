import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors-skpi-list")
        chrome_options.add_argument("--disable-popup-blocking")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors-skpi-list")
        chrome_options.add_argument("--disable-popup-blocking")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.google.com")

    request.cls.driver = driver
    yield
    driver.close()

