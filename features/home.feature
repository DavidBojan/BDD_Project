Feature: homepage functionality

  Scenario: altex homepage title and search title
    Given home: I am a user on altex.ro Home page
    When home: I am checking the home page for header title
    Then home: the search box field is displayed
    And home: the url is "https://altex.ro/home/"
