__author__ = 'i20764'

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class DragDrop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Edge("D:\\Sujan Sauden\\codes\\edgedriver_win64\\IEDriverServer.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_verify_drag_drop(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/drag_and_drop")

        # action = ActionChains(driver)

        source_element = driver.find_element_by_css_selector("div#column-a")

        target_element = driver.find_element_by_css_selector("div#column-b")

        ActionChains(driver).drag_and_drop(source_element,target_element).perform()
        # action.click_and_hold(source_element).move_to_element(target_element).release(target_element).perform()




if __name__ == '__main__':
    unittest.main




