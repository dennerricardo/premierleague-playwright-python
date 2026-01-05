import pytest
from playwright.sync_api import Playwright
from pages.dashboard_page import DashboardPage

@pytest.fixture(scope="session")
def browserInstance(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    dashboardPg = DashboardPage(page)

    yield dashboardPg

    context.close()
    browser.close()

