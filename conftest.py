from pathlib import Path
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from config.settings import BROWSER, HEADLESS, EXPLICIT_WAIT, PAGE_LOAD_TIMEOUT

def create_driver():
    if BROWSER == "chrome":
        options = ChromeOptions()
        if HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,900")
        driver = webdriver.Chrome(options=options)
    elif BROWSER == "firefox":
        options = FirefoxOptions()
        if HEADLESS:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    elif BROWSER == "edge":
        options = EdgeOptions()
        if HEADLESS:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError("BROWSER must be chrome, firefox, or edge.")
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    return driver

@pytest.fixture
def driver():
    d = create_driver()
    yield d
    d.quit()

@pytest.fixture
def login_page(driver):
    from pages.login_page import LoginPage
    return LoginPage(driver, EXPLICIT_WAIT).load()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    driver = item.funcargs.get("driver")
    if driver:
        path = Path("artifacts/screenshots")
        path.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(str(path / f"{item.name}_{stamp}.png"))
