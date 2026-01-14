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
        goals_table = self.page.locator("ul[class='stats-leaderboard__leaderboard']").first
        rows = goals_table.locator("li[class='stats-leaderboard__stat-wrapper']")
        row_count = rows.count()
        print(f"rows count: {row_count}")

        print("Player\tTeam\tGoals")

        for i in range(row_count):
            player = rows.nth(i).locator("span[class='stats-leaderboard__name']").text_content()
            team = rows.nth(i).locator("span[class='stats-leaderboard__team-name u-hide-desktop']").text_content()
            goals = rows.nth(i).locator("span[class='stats-leaderboard__stat-value']").text_content()

            print(f"{player}\t{team}\t{goals}")

    def assists_list(self):
        assists_table = self.page.locator("ul[class='stats-leaderboard__leaderboard']").nth(1)
        rows = assists_table.locator("li[class='stats-leaderboard__stat-wrapper']")
        row_count = rows.count()
        print(f"rows count: {row_count}")

        print("Player\tTeam\tAssists")

        for i in range(row_count):
            player = rows.nth(i).locator("span[class='stats-leaderboard__name']").text_content()
            team = rows.nth(i).locator("span[class='stats-leaderboard__team-name u-hide-desktop']").text_content()
            assists = rows.nth(i).locator("span[class='stats-leaderboard__stat-value']").text_content()

            print(f"{player}\t{team}\t{assists}")


    def total_passes_list(self):
        total_passes_table = self.page.locator("ul[class='stats-leaderboard__leaderboard']").nth(2)
        rows = total_passes_table.locator("li[class='stats-leaderboard__stat-wrapper']")
        row_count = rows.count()
        print(f"rows count: {row_count}")

        print("Player\tTeam\tTotal Passes")

        for i in range(row_count):
            player = rows.nth(i).locator("span[class='stats-leaderboard__name']").text_content()
            team = rows.nth(i).locator("span[class='stats-leaderboard__team-name u-hide-desktop']").text_content()
            total_passes = rows.nth(i).locator("span[class='stats-leaderboard__stat-value']").text_content()

            print(f"{player}\t{team}\t{total_passes}")

    def clean_sheets_list(self):
        clean_sheets_table = self.page.locator("ul[class='stats-leaderboard__leaderboard']").nth(3)
        rows = clean_sheets_table.locator("li[class='stats-leaderboard__stat-wrapper']")
        row_count = rows.count()
        print(f"rows count: {row_count}")

        print("Player\tTeam\tClean Sheets")

        for i in range(row_count):
            player = rows.nth(i).locator("span[class='stats-leaderboard__name']").text_content()
            team = rows.nth(i).locator("span[class='stats-leaderboard__team-name u-hide-desktop']").text_content()
            clean_sheets = rows.nth(i).locator("span[class='stats-leaderboard__stat-value']").text_content()

            print(f"{player}\t{team}\t{clean_sheets}")

