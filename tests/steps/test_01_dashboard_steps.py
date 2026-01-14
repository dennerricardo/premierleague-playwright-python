from playwright.sync_api import expect
from pytest_bdd import given,scenarios, when, then

scenarios('features/dashboard.feature')

@given('user navigates to the Premier League stats page')
def test_navigate_premier_dashboard(browserInstance):
   browserInstance.navigate()
   print(browserInstance.page.title)
   expect(browserInstance.page).to_have_url('https://www.premierleague.com/en/stats')

@given('user validates dashboard page title')
def test_validates_dashboard_page_title(browserInstance):
    print(browserInstance.page.title)
    expect(browserInstance.page).to_have_title('Premier League Player Stats & Club Statistics')

@when('the statistics dashboard is displayed')
def test_statistics_dashboard_displayed(browserInstance):
    expect(browserInstance.playerstats_title).to_be_visible()
    print(browserInstance.playerstats_title)

@then('the dashboard should show the Goals category')
def test_validates_goals_category(browserInstance):
    expect(browserInstance.goal_title).to_be_visible()
    print(browserInstance.goal_title)
    # expect(browserInstance.page).to_have_title('Premier League First Team Club Statistics, Team & Player Stats')

@then('the dashboard should show the Assists category')
def test_validates_assists_category(browserInstance):
    expect(browserInstance.assists_title).to_be_visible()
    print(browserInstance.assists_title)

@then('the dashboard should show the Clean Sheets category')
def test_validates_cleansheets_category(browserInstance):
    expect(browserInstance.cleansheets_title).to_be_visible()
    print(browserInstance.cleansheets_title.first)

@then('the dashboard should show the Total Passes category')
def test_validates_totalpasses_category(browserInstance):
    expect(browserInstance.totalpasses_title).to_be_visible()
    print(browserInstance.totalpasses_title.first)


@then('a list of players should be displayed')
def test_list_of_players(browserInstance):
    browserInstance.goals_list()






