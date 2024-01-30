import pytest
from selene import browser

@pytest.fixture(autouse=True)
def setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'


    yield

    browser.quit()
