Feature: login functionality
  Background:
    Given home: I am a user on amazon.com Home page
  Scenario:
    When home: I click on Sign in
    When login: I set my email "davidtstacct@gmail.com" and click Continue
    When login: I set my password "aMaz7!on" and click on Sign in
    Then home: the Hello message is displayed