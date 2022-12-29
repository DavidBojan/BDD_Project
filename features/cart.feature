Feature: Amazon cart feature

    Background:
      Given home: I am a user on amazon.com Home page
      When home: I search product after phone "Xiaomi Redmi Note 11 4G Volte 128GB + 4GB Factory Unlocked 6.43"
      When products: I click on phone "Xiaomi Redmi Note 11 4G Volte 128GB + 4GB Factory Unlocked 6.43"
      When products: I click on "Add to cart"
      When home: I click on cart

    @cart
    Scenario: Test cart remove product functionality
      When cart: I click Delete
      Then cart: I verify empty cart message is displayed
