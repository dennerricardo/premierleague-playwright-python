from playwright.sync_api import Page

class DashboardPage:

    def __init__(self, page: Page):
        self.page = page


    def navigate(self):
        self.page.goto("https://www.premierleague.com/en/stats")

