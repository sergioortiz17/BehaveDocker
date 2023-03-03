from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.debug('Starting script...')

@given('I am on the Google home page')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('no-sandbox')
    chrome_options.add_argument('disable-setuid-sandbox')
    chrome_options.add_argument('window-size=1920,1200')
    chrome_options.add_argument('ignore-certificate-errors')
    chrome_options.add_argument('allow-running-insecure-content')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument('disable-gpu')
    chrome_options.add_argument('disable-extensions')
    chrome_options.add_argument('disable-dev-shm-usage')

    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    context.driver = driver

    context.driver.maximize_window()
    context.driver.get("https://www.google.com")

@when('I enter "{search_query}" in the search bar')
def step_impl(context, search_query):
    element = context.driver.find_element_by_name("q")
    element.clear()
    element.send_keys(search_query)

@when('I click the "Google Search" button')
def step_impl(context):
    button = context.driver.find_element_by_name("btnK")
    button.click()

@then('I should see search results for "{search_query}"')
def step_impl(context, search_query):
    assert search_query in context.driver.title

    context.driver.quit()
