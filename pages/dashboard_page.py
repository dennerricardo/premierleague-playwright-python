from playwright.sync_api import Page

class DashboardPage:

    def __init__(self, page: Page):
        self.page = page
        self.playerstats_title = page.get_by_text("Premier League 2025/26 Player Stats")
        self.goal_title = page.get_by_text("Goals").first
        self.assists_title = page.get_by_text("Assists")
        self.totalpasses_title = page.get_by_text("Total Passes").first
        self.cleansheets_title = page.get_by_text("Clean Sheets")


    def navigate(self):
        self.page.goto("https://www.premierleague.com/en/stats")

