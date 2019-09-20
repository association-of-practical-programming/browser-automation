from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

browser = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)

browser.get('https://www.google.com')

search_input = browser.find_element_by_xpath(
    '//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')

search_input.send_keys('weather')

search_button = browser.find_element_by_xpath(
    '//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]')

search_button.click()

cel_button = browser.find_element_by_xpath(
    '//*[@id="wob_d"]/div/div[1]/div/div[2]/a[2]')

cel_button.click()

temp_text = browser.find_element_by_id('wob_ttm')

tempOutside = temp_text.get_attribute('innerText')

print(tempOutside)

browser.close()
