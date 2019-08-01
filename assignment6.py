__author__ = 'i20764'

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class WindowHandle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://the-internet.herokuapp.com/windows")


    def test_window_handle(self):
        driver = self.driver
        for i in range(5):
            driver.find_element(By.XPATH,"//div[@class = 'example']/a").click()
            driver.back()
        self.assertEqual(len(driver.window_handles),6,"Pass")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main
