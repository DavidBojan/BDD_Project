from behave import *


@when('products: I click on "{product_name}"')
def step_impl(context, product_name):
    context.products_page.click_on_product(product_name)


@then('products: I click on "Add to cart"')
def step_impl(context):
    context.products_page.add_to_cart()


@then('products: I verify that results contain search query "{query}"')
def step_impl(context, query):
    context.products_page.verify_results_contain_text(query)
