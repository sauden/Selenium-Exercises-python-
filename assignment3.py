__author__ = 'i20764'
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HoverAction(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://the-internet.herokuapp.com/hovers')
        self.driver.maximize_window()

    def test_hover_user(self):
        i = 1
        while i < 4:
            element = self.driver.find_element(By.XPATH,'//div[@class=\'figure\'][' + str(i) + ']')
            hoverover = ActionChains(self.driver).move_to_element(element).perform()

            element1 = self.driver.find_element(By.XPATH,'//div[@class=\'figure\'][' + str(i) + ']//a').click()
            self.assertEqual(self.driver.current_url[-1],str(i))
            self.driver.back()
            i += 1

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main



