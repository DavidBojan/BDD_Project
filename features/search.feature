Feature: Amazon search feature

    Background:
      Given home: I am a user on amazon.com Home page

    @search
    Scenario Outline: Test search functionality
      When home: I search after "<query>"
      Then products: I verify that results contain search query "<query>"

    Examples:
      | query   |
      | xiaomi  |
      | philips |