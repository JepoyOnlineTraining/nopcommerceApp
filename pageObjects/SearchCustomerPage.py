from selenium.webdriver.common.by import By


class SearchCustomerPage:
    field_searh_email_id = "SearchEmail"
    field_firstname_id = "SearchFirstName"
    field_lastname_id = "SearchLastName"
    button_search_id = "search-customers"
    table_customer_grid_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    data_email_xpath = "//table[@id='customers-grid']//tbody//tr[1]/td[2]"
    data_name_xpath = "//table[@id='customers-grid']//tbody//tr[1]/td[3]"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.field_searh_email_id).clear()
        self.driver.find_element(By.ID, self.field_searh_email_id).send_keys(email)

    def setFirstname(self, firstname):
        self.driver.find_element(By.ID, self.field_firstname_id).clear()
        self.driver.find_element(By.ID, self.field_firstname_id).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.ID, self.field_lastname_id).clear()
        self.driver.find_element(By.ID, self.field_lastname_id).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.button_search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_columns_xpath))

    def verifySearchTable(self):
        search_table = self.driver.find_element(By.XPATH, self.table_customer_grid_xpath)
        if search_table:
            assert True
        else:
            assert False

    def verifyEmailAddress(self, user_email):
        email = self.driver.find_element(By.XPATH, self.data_email_xpath).text
        if user_email in email:
            assert True
        else:
            assert False

    def verifName(self, user_name):
        name = self.driver.find_element(By.XPATH, self.data_name_xpatha).text
        if user_name in name:
            assert True
        else:
            assert False

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_customer_grid_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+ str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCutomerByName(self, fullname):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_customer_grid_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+ str(r)+"]/td[3]").text
            if name == fullname:
                flag = True
                break
        return flag


