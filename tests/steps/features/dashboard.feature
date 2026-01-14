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

  Scenario: Display list for goals
      Given user navigates to the Premier League stats page
      Then a list of goals should be displayed

  Scenario: Display list for assists
      Given user navigates to the Premier League stats page
      Then a list of assists should be displayed

  Scenario: Display list for total passes
      Given user navigates to the Premier League stats page
      Then a list of total passes should be displayed

  Scenario: Display list for clean Sheets
      Given user navigates to the Premier League stats page
      Then a list of clean sheets should be displayed

