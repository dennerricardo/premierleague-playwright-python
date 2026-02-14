import pytest
from playwright.sync_api import Playwright
from tests.utils.goals_api_client import generate_players_json

@pytest.fixture(scope="session")
def browserInstance(playwright : Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()



@pytest.fixture(scope="session")
def players_file():
    return generate_players_json()

