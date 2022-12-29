from behave import *


@given('home: I am a user on amazon.com Home page')
def step_impl(context):
    context.home_page.navigate_to_home_page()


@when('home: I am checking for the home page header title')
def step_impl(context):
    context.home_page.home_page_title()


@when('home: the search box field is displayed')
def step_impl(context):
    context.home_page.search_box()


@then('home: the sign in button is displayed')
def step_impl(context):
    context.home_page.sign_in_button_displayed()


@when('home: I click on Sign in')
def step_impl(context):
    context.home_page.click_sign_in_button()


@then('home: the Hello message is displayed')
def step_impl(context):
    context.home_page.hello_message()


@when('home: I search after "{query}"')
def step_impl(context, query):
    context.home_page.search_after(query)


@when('home: I search product after phone "{product}"')
def step_impl(context, product):
    context.home_page.search_product(product)


@when('home: I click on cart')
def step_impl(context):
    context.home_page.click_on_cart()
