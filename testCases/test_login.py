import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import allure


# To run the test by group
# pytest -v -s -m "sanity" --html=./Reports/report.html testCases/ --browser chrome

@allure.severity(allure.severity_level.NORMAL)
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********** Test_001_Login ********")
        self.logger.info("********** Verifying Home Page Title ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Home Page title is PASSED ********")
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testTitlePage",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(filename=".//Screenshots//" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Home Page title is FAILED ********")
            assert False, f"Invalid title: {act_title}"

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********** Verifying Login test ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(username=self.username)
        self.lp.setPassword(password=self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(5)
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("********** Login test PASSED ********")
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen",
                          attachment_type=AttachmentType.png)
            self.driver.save_screenshot(filename=".//Screenshots//" + "test_login.png")
            self.logger.error("********** Login test FAILED ********")
            self.driver.close()
            assert False, f"Invalid title {act_title}"
