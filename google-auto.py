from selenium import webdriver
browser = webdriver.Chrome('./chromedriver')

browser.get('http://www.google.com')

searchBar = browser.find_element_by_xpath(
    '//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')

searchBar.send_keys('weather')
