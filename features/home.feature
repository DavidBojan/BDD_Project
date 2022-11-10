Feature: homepage functionality
  Scenario: homepage is working
    Given home: I am a user on amazon.com Home page
    When home: I am checking for the home page header title
    When home: the search box field is displayed
    Then home: the sign in button is displayed
