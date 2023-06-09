import time

import pytest

from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********** SearchCustomerByEmaik **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("********* Login successful **********")
        self.logger.info("********** Starting Search Customer By Email *********")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomerLink()


        self.logger.info("********** searching customer by emailID **********")

        self.searchcust = SearchCustomerPage(self.driver)
        self.searchcust.setEmail("kiyjcycyhjc676008@gmail.com")
        self.searchcust.clickSearch()

        time.sleep(3)

        status = self.searchcust.searchCustomerByEmail("kiyjcycyhjc676008@gmail.com")
        assert True == status
        self.logger.info("********** TC_SearchCustomerByEmail_004 Finished **********")

        self.driver.close()
