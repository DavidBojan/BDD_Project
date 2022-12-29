Feature: Amazon cart feature

    Background:
      Given home: I am a user on amazon.com Home page
      When home: I search product after "Xiaomi Redmi Note 11 4G Volte 128GB + 4GB Factory Unlocked 6.43"
      When products: I click on  "Xiaomi Redmi Note 11 4G Volte 128GB + 4GB Factory Unlocked 6.43"
      Then products: I click on "Add to cart"

    @cart1
    Scenario: Test cart total sum functionality
      Then cart: I verify that total price is correct "180.70"


    @cart2
    Scenario: Test cart remove product functionality
      When cart: I click sterge link
      Then cart: I verify empty cart message is displayed
