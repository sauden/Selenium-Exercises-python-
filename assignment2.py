__author__ = 'i20764'
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os

class FileUpload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://the-internet.herokuapp.com/upload")
        self.fileName = 'pranesh-gautam.jpg'
        self.fullPath = os.path.abspath(self.fileName)
        print(self.fullPath)

    def test_file_upload(self):
        element = self.driver.find_element(By.CSS_SELECTOR,"input#file-upload[type=file]").send_keys(self.fullPath)

        self.driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()

        # check search field exists on Images page
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"div#uploaded-files"))

        uploadedFileName = self.driver.find_element(By.CSS_SELECTOR,"div#uploaded-files").text

        self.assertEqual(uploadedFileName,self.fileName)



    def tearDown(self):
        self.driver.close()

    def is_element_present(self,how,what):
        try: self.driver.find_element(by = how,value= what)
        except NoSuchElementException: return False
        return True

if __name__ == '__main__':
    unittest.main

