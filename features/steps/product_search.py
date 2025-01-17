from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# SEARCH_INPUT = (By.NAME, 'q')
# SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon page')
def open_google(context):
    # context.driver.get('https://www.google.com/')
    context.app.main_page.open_main()


@given('Open Amazon outlet page')
def open_amazon_outlet(context):
    context.app.main_page.open_outlet()


@given('Open Amazon product page')
def open_amazon_product(context):
    context.app.main_page.open_product()

@when('Input {search_word} into search field')
def input_search(context, search_word):
    # search = context.driver.find_element(*SEARCH_INPUT)
    # search.clear()
    # search.send_keys(search_word)
    # sleep(4)
    context.app.header.input_search_text(search_word)


@when('Click on search icon')
def click_search_icon(context):
    # context.driver.find_element(*SEARCH_SUBMIT).click()
    # sleep(1)
    context.app.header.click_search()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"


@then('Search results for {search_word} are shown')
def verify_search_result(context, search_word):
    context.app.search_results_page.verify_search_result(search_word)
