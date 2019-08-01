__author__ = 'i20764'
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By

class TestTable(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://the-internet.herokuapp.com/tables')
        self.driver.maximize_window()

    def test_table_sorting(self):
        justClickAtFirstHeader = self.driver.find_element(By.XPATH,'//table[@id="table1"]//tr/th[1]/span').click()
        allData = []
        sortedListIs = []

        listAfterClickSecondClick = self.driver.find_element(By.XPATH,'//table[@id = "table1"]/tbody/tr/td[1]')
        listOfDataText = listAfterClickSecondClick.text

        for i in range(1,len(listOfDataText)+1):
            allData.append(self.driver.find_element(By.XPATH,'//table[@id = "table1"]/tbody/tr['+str(i)+']/td[1]').text)

        for x in sorted(allData):
            sortedListIs.append(x)

        for i in range(0,len(allData)):
            self.assertEqual(sortedListIs[i],allData[i],"pass")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main













