import logging.config
from os import path


lof_file_path = path.join(path.dirname(path.abspath(__file__)), "logging.ini")
logging.config.fileConfig(lof_file_path)

pytest_plugins = ["src.fixtures.system.browser"]


def pytest_addoption(parser):
    parser.addini("selenium_url", "Selenium Hub Url")
    # parser.addini("browser_name", "Browser Name for Tests")
    parser.addini("browser_version", "Browser Version for Tests")
    parser.addini("headless", "Hidden mod for browser")
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser name: chrome, firefox, safari, etc."
    )
