import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("headless")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-popup-blocking")
        # chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser_name == "IE":
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))

    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("headless")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-popup-blocking")
        # chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    # driver.get("https://qaclickacademy.github.io/protocommerce/")
    driver.get("https://www.playstation.com/en-in/games/dead-island-2/")
    request.cls.driver = driver
    yield
    driver.close()


# @pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
