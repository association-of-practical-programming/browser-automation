from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import json

import time

with open("./cred.json", "r") as f:
    data = json.loads(f.read())
    print(data)

# chrome_options = Options()
# chrome_options.add_argument("--headless")

browser = webdriver.Chrome("./chromedriver")

browser.get('https://www.twitter.com')

login_button = browser.find_element_by_xpath(
    '//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]')

login_button.click()

time.sleep(3)

user = browser.find_element_by_xpath(
    '//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
password = browser.find_element_by_xpath(
    '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')

user.send_keys(data.get("number"))
password.send_keys(data.get("password"))

button = browser.find_element_by_xpath(
    '//*[@id="page-container"]/div/div[1]/form/div[2]/button')

button.click()
