from behave import *
from selenium import webdriver

@given('I am on the Poczta tab of wp.pl')
def step_impl(context):
    context.browser = webdriver.Firefox()
    context.browser.get("https://www.poczta.wp.pl")
@when('I log in by using {login} and {password}')
def step_impl(context, login, password):
    login_input = context.browser.find_element_by_xpath('//*[@id="login"]')
    login_input.clear()
    login_input.send_keys(login)
    password_input = context.browser.find_element_by_xpath('//*[@id="password"]')
    password_input.clear()
    password_input.send_keys(password)
    zaloguj = context.browser.find_element_by_xpath('//*[@id="btnSubmit"]')
    zaloguj.click()
@then('I {is_logged_in} logged in in to poczta')
def step_impl(context, is_logged_in):
    if is_logged_in == 'am':
        assert "Wyloguj" in context.browser.page_source
        context.browser.quit()
    elif is_logged_in == 'am not':
        assert "Załóż konto" in context.browser.page_source
        context.browser.quit()
    else:
        pass