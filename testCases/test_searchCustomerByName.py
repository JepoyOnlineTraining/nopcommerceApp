import time
import pytest
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByName:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_searchCustomerByName(self, setup):
        self.logger.info("********** SearchCustomerByEmaik **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("********* Login successful **********")
        self.logger.info("********** Starting Search Customer By Name *********")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomerLink()

        self.logger.info("********** searching customer by Name **********")

        self.searchcust = SearchCustomerPage(self.driver)
        self.searchcust.setFirstname("Virat")
        self.searchcust.setLastname("Kohli")
        self.searchcust.clickSearch()

        time.sleep(3)

        status = self.searchcust.searchCutomerByName("Virat Kohli")
        assert True == status
        self.logger.info("********** TC_SearchCustomerByName_005 Finished **********")

        self.driver.close()
