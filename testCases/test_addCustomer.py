import random
import string

import pytest

from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


# pytest -s -v -m "sanity" --html=Reports\report.html testCases/ --browser=chrome


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login succesful *********")
        self.logger.info("********** Starting Add Customer Test **********")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomerLink()
        self.addcust.clickAddNewButton()

        self.logger.info("********** Providing customer information **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Jann")
        self.addcust.setLastName("Reyes")
        self.addcust.selectGender()
        self.addcust.setDataOfBirth("11/21/2022")
        self.addcust.setCompanyName("Don Sorbetest")
        self.addcust.setTaxExempt()
        self.addcust.setNewsLetter("Your store name")
        self.addcust.setCustomerRoles("Administrators")
        self.addcust.setManageVendor("Vendor 1")
        self.addcust.setActive()
        self.addcust.setComment("Jann Geo is Pogi")
        self.addcust.clickSave()
        self.addcust.verifySuccessMessage()
        self.driver.quit()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
