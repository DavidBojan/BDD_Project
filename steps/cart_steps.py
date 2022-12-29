from behave import *


@when('cart: I click Delete')
def step_impl(context):
    context.cart_page.click_on_delete()


@then('cart: I verify empty cart message is displayed')
def step_impl(context):
    context.cart_page.empty_cart_msg()

