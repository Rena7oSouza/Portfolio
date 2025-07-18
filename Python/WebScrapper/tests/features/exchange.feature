Feature: USD-BRL exchange rate scraping

  Scenario: Get current USD-BRL exchange rate
    Given I access the exchange scraper
    When I get the USD-BRL rate
    Then the rate should be a valid number
