from playwright.sync_api import expect
from pytest_bdd import given,scenarios

scenarios('dashboard.feature')

@given('user navigates to the Premier League stats page')
def test_navigate_premier_dashboard(browserInstance):
   browserInstance.navigate()
   print(browserInstance.page.url)
   expect(browserInstance.page).to_have_url('https://www.premierleague.com/en/stats')

@given('user validates dashboard page title')
def test_validates_dashboard_page_title(browserInstance):
    print(browserInstance.page.title)
    expect(browserInstance.page).to_have_title('Premier League First Team Club Statistics, Team & Player Stats')






