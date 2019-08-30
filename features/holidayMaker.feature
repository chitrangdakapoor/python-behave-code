Feature: Test Holiday Maker
  Scenario: A happy holidaymaker
    Given I like to holiday in "Sydney" on "Thursdays"
    And If today is "Thursday"
    When I look up the weather forecast
    Then check the temperature is warmer than "10" degrees
