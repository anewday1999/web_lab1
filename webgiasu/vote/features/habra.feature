Feature: Habrarating

  Scenario: Show a rating
    Given I am a visitor
    When I visit url "http://localhost:8000/"
    Then I should see link contents url "habrahabr.ru"