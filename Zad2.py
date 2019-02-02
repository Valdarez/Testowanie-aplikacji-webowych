import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class WizzairRegisteration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_register_wizzair_com(self):
        browser = self.browser
        browser.get("http://www.wizzair.com")

        login = browser.find_element_by_xpath('//*/header/div[1]/div/div/button')
        #login.click()
        browser.execute_script("arguments[0].click();",login)

        registration = browser.find_element_by_xpath('//*/form/div/p/button')
        #registration.click()
        browser.execute_script("arguments[0].click();", registration)

        firstname = browser.find_element_by_name("firstName")
        firstname.send_keys("qwerty")

        lastname = browser.find_element_by_xpath('//*/label[2]/div[1]/input')
        lastname.send_keys("asdfgh")

        gender = browser.find_element_by_xpath('//*/div[1]/label[2]/span')
        browser.execute_script("arguments[0].click();", gender)

        phone = browser.find_element_by_name("mobilePhone")
        phone.send_keys("123456789")

        email_niepoprawny = browser.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[1]/label/input')
        email_niepoprawny.send_keys("asdfgh@wp.pl")

        password = browser.find_element_by_xpath('//*[@id="regmodal-scroll-hook-5"]/div[1]/label/input')
        password.send_keys("qwerty123456")

        checkbox = browser.find_element_by_xpath('//*/form/div[2]/div[10]/span/label[1]')
        browser.execute_script("arguments[0].click();", checkbox)

        register = browser.find_element_by_xpath('//*/form/div[2]/div[11]/button')
        browser.execute_script("arguments[0].click();", register)

        hidden_element = browser.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[2]/span/span')
        self.assertTrue("Informacja, o niepoprawnym adresie e-mail", hidden_element.is_displayed())

if __name__ == "__main__": unittest.main()