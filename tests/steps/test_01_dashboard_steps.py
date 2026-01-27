import pytest

from playwright.sync_api import expect , Page
from pytest_bdd import given,scenarios, when, then
from pytest_html import extras as html_extras

from pages.dashboard_page import DashboardPage

scenarios('features/dashboard.feature')

@pytest.fixture(scope="function")
def dashboard_page(browserInstance):
    return DashboardPage(browserInstance)


@given('user navigates to the Premier League stats page')
def navigate_premier_dashboard(dashboard_page):
   dashboard_page.navigate()
   print(dashboard_page.page.url)
   expect(dashboard_page.page).to_have_url('https://www.premierleague.com/en/stats')

@given('user validates dashboard page title')
def validates_dashboard_page_title(dashboard_page):
    print(dashboard_page.page.title())
    expect(dashboard_page.page).to_have_title('Premier League Player Stats & Club Statistics')

@when('the statistics dashboard is displayed')
def statistics_dashboard_displayed(dashboard_page):
    expect(dashboard_page.playerstats_title).to_be_visible()
    print(dashboard_page.playerstats_title.text_content())


@then('the dashboard should show the Goals category')
def validates_goals_category(dashboard_page ):
    expect(dashboard_page.goal_title).to_be_visible()
    print(dashboard_page.goal_title.text_content())
    # expect(browserInstance.page).to_have_title('Premier League First Team Club Statistics, Team & Player Stats')

    screenshot_path = "screenshots/goals_dashboard.png"
    dashboard_page.page.screenshot(path=screenshot_path)

@then('the dashboard should show the Assists category')
def validates_assists_category(dashboard_page):
    expect(dashboard_page.assists_title).to_be_visible()
    print(dashboard_page.assists_title.text_content())
    # dashboard_page.assists_title.screenshot(path="report/assist_list.png")

@then('the dashboard should show the Clean Sheets category')
def validates_cleansheets_category(dashboard_page):
    expect(dashboard_page.cleansheets_title).to_be_visible()
    print(dashboard_page.cleansheets_title.text_content())

@then('the dashboard should show the Total Passes category')
def validates_totalpasses_category(dashboard_page):
    expect(dashboard_page.totalpasses_title).to_be_visible()
    print(dashboard_page.totalpasses_title.text_content())

@then('a list of goals should be displayed')
def list_of_goals(dashboard_page):
    dashboard_page.goals_list()

@then('a list of assists should be displayed')
def list_of_assists(dashboard_page):
    dashboard_page.assists_list()

@then('a list of total passes should be displayed')
def list_of_total_passes(dashboard_page):
    dashboard_page.total_passes_list()

@then('a list of clean sheets should be displayed')
def list_of_clean_sheets(dashboard_page):
    dashboard_page.clean_sheets_list()







