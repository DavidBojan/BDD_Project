from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.home_page import HomePage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.login_page = LoginPage()
    context.products_page = ProductsPage()


def after_all(context):
    context.browser.close()
