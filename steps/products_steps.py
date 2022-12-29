from behave import *


@then('products: I verify that results contain search query "{query}"')
def step_impl(context, query):
    context.products_page.verify_results_contain_text(query)


@when('products: I click on phone "{product}"')
def step_impl(context, product):
    context.products_page.click_on_product(product)


@when('products: I click on "Add to cart"')
def step_impl(context):
    context.products_page.add_to_cart()
