import os

import pytest
from playwright.sync_api import Playwright



@pytest.fixture(scope="session")
def browserInstance(playwright : Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()


