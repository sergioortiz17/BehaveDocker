Feature: Google Search

  Scenario: Search for 'Pruebas de automatización con Selenium'
    Given I am on the Google home page
    When I enter 'Pruebas de automatización con Selenium' in the search bar
    And I click the 'Google Search' button
    Then I should see search results for 'Pruebas de automatización con Selenium'
