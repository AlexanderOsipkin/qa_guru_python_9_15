import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from metro_tests_suite.utils import attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': "100.0",
        'selenoid:options': {'enableVNC': True, 'enableVideo': True},
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f'https://user1:1234@selenoid.autotests.cloud/wd/hub',
        options=options,
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://online.metro-cc.ru/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
