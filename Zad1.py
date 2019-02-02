from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest2

browser = webdriver.Firefox()
browser.get("http://duckduckgo.com")
elem = browser.find_element_by_id("search_form_input_homepage")
elem.clear()
elem.send_keys("the biggest python software house")
elem.send_keys(Keys.RETURN)
wait = WebDriverWait(browser, 2)

try:
text = "STX Next"
#div = browser.find_element_by_id("r1-0")
assert text in browser.page_source

except AssertionError:
print(text+" was found.")

browser.close()