Feature: Stats Center Dashboard
    Test related to access to stats center dashboard


  Scenario: Access the stats center dashboard
    Given user navigates to the Premier League stats page
    And user validates dashboard page title

  Scenario: Display player statistics categories
    When the statistics dashboard is displayed
    Then the dashboard should show the Goals category
    And the dashboard should show the Assists category
    And the dashboard should show the Total Passes category
    And the dashboard should show the Clean Sheets category

  Scenario: Display player list for goals statistics
      Given user navigates to the Premier League stats page
      Then a list of players should be displayed

#  Scenario: Display player list for assists statistics
#      When the player statistics dashboard is displayed
#      Then a list of players should be displayed
#      And each player entry should show the player name
#      And each player entry should show the team name
#      And each player entry should show the goals value
#
#
#  Scenario: Display player list for total passes statistics
#      When the player statistics dashboard is displayed
#      Then a list of players should be displayed
#      And each player entry should show the player name
#      And each player entry should show the team name
#      And each player entry should show the goals value
#
#
#  Scenario: Display player list for clean sheets statistics
#      When the player statistics dashboard is displayed
#      Then a list of players should be displayed
#      And each player entry should show the player name
#      And each player entry should show the team name
#      And each player entry should show the goals value