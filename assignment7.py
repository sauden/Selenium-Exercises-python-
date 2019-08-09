__author__ = 'i20764'
import unittest
from selenium import  webdriver
from selenium.webdriver.common.by import By
import os


class FileDownload(unittest.TestCase):
    def setUp(self):
        self.dir = os.path.dirname("D:\\Sujan Sauden\\codes\\chromedriver_win32\\")
        self.chrome_driver_path = self.dir + "\\" + "chromedriver.exe"
        # create a new Firefox session
        print(self.chrome_driver_path)
        self.driver = webdriver.Chrome(self.chrome_driver_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("http://the-internet.herokuapp.com/download")

    def test_file_download(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT,"empty.txt").click()
