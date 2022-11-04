from behave import *


@given('home: I am a user on altex.ro Home page')
def step_impl(context):
    context.home_page.navigate_to_home_page()
    context.home_page.click_accept_cookies_btn()
    context.home_page.click_newsletter_close_btn()


@when('I am checking the home page for header title')
def step_impl(context):
    context.home_page.home_page_title()


@then('the search box field is displayed')
def step_impl(context):
    context.home_page.search_box()


@then('the url is "https://altex.ro/home/"')
def step_imp(context):
    context.verify_url_message()
