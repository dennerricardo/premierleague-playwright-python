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


    def goals_list(self):
        goals_table = self.page.locator("ul.stats-leaderboard__leaderboard").first
        rows = goals_table.locator("li")
        row_count = rows.count()
        print(f"rows count: {row_count}")

        print("Player\tTeam\tGoals")

        for i in range(row_count):
            player = rows.nth(i).locator("span.stats-leaderboard__name").text_content()
            team = rows.nth(i).locator("span.stats-leaderboard__team-name u-hide-desktop").text_content()
            goals = rows.nth(i).locator("span.stats-leaderboard__stat-value").text_content()

            print(f"{player}\t{team}\t{goals}")


