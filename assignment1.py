__author__ = 'i20764'
# -*- coding: UTF-8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class MessageDisappear(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://the-internet.herokuapp.com/dynamic_loading/2")

    def test_click_start(self):
        element = self.driver.find_element(By.CSS_SELECTOR,'#start>button')
        element.click()

        #implemented explicit wait
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#finish h4")))

        # check search field exists on Images page
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"div#finish h4"))

        #find the value of that element
        result = self.driver.find_element_by_css_selector('div#finish h4').text

        #print element value
        print(result)

        #comparing the value of element with expected
        self.assertEqual(result, "Hello World!","Failed")


    def tearDown(self):
        self.driver.close()

    def is_element_present(self, how, what):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True

if __name__ == '__main__':
    unittest.main()



