from behave import *


@when('login: I set my email "davidtstacct@gmail.com" and click Continue')
def step_impl(context):
    context.login_page.set_email()
    context.login_page.click_continua_btn()


@when('login: I set my password "aMaz7!on" and click on Sign in')
def step_impl(context):
    context.login_page.set_password()
    context.login_page.click_sign_in_btn()
