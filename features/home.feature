Feature: homepage functionality

  Scenario: altex homepage title and search title
    Given home: I am a user on altex.ro Home page
    When I am checking the home page for header title
    Then the search box field is displayed
    Then the url is "https://altex.ro/home/"