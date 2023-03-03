from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('no-sandbox')
    chrome_options.add_argument('disable-setuid-sandbox')
    chrome_options.add_argument('window-size=1920,1200')
    chrome_options.add_argument('ignore-certificate-errors')
   
