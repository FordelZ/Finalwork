from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import pytest


@pytest.fixture(scope="class")
def selenium(pytestconfig):
    options = Options()
    options.page_load_strategy = 'normal'
    browser_name = pytestconfig.getoption("browser_name")
    logging.info(f"Prepare {browser_name} browser...")
    if pytestconfig.getini("headless") == "False" and browser_name == "chrome":
        options.add_argument("headless")

    driver = webdriver.Remote(
        command_executor=pytestconfig.getini("selenium_url"),
        options=options
    )
    driver.implicitly_wait(20)
    logging.info(f"Browser {browser_name} has been started...")
    yield driver
    pass
