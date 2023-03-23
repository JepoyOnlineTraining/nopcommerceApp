import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomerPage:
    # Locators
    link_customer_xpath = "//a[@href='#']//p[contains(.,'Customers')]"
    subLink_customer_xpath = "//a[@href='/Admin/Customer/List']//p[contains(.,'Customers')]"
    button_add_new_customer_xpath = "//a[@href='/Admin/Customer/Create']"

    field_email_id = "Email"
    field_password_id = "Password"
    field_firstname_id = "FirstName"
    field_lastname_id = "LastName"
    radio_gender_male_id = "Gender_Male"
    radio_gender_female_id = "Gender_Female"
    field_date_of_birth_id = "DateOfBirth"
    field_company_name_id = "Company"
    field_test_id = "customer_attribute_1"
    cbox_is_tax_exempt_id = "IsTaxExempt"
    input_news_letter_xpath = "//input[@aria-labelledby='SelectedNewsletterSubscriptionStoreIds_label']"
    list_news_letter_option_1_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    list_news_letter_option_2_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    input_customer_roles_xpath = "//input[@aria-labelledby='SelectedCustomerRoleIds_label']"
    # list_customer_roles_option_1_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    list_customer_roles_option_1_xpath = "//li[contains(text(), 'Administrator')]"
    list_customer_roles_option_2_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    list_customer_roles_option_3_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    list_customer_roles_option_4_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    list_customer_roles_option_5_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    dropdown_vendor_id = "VendorId"
    cbox_active_id = "Active"
    field_comment_id = "AdminComment"
    label_success_message_xpath = "//div[@class='alert alert-success alert-dismissable']"

    button_save_xpath = "//button[@name= 'save']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.link_customer_xpath).click()

    def clickCustomerLink(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.subLink_customer_xpath).click()

    def clickAddNewButton(self):
        self.driver.find_element(By.XPATH, self.button_add_new_customer_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.field_email_id).clear()
        self.driver.find_element(By.ID, self.field_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.field_password_id).clear()
        self.driver.find_element(By.ID, self.field_password_id).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.field_firstname_id).clear()
        self.driver.find_element(By.ID, self.field_firstname_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.field_lastname_id).clear()
        self.driver.find_element(By.ID, self.field_lastname_id).send_keys(lastname)

    def selectGender(self, gender="male"):
        if gender == "male":
            self.driver.find_element(By.ID, self.radio_gender_male_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_gender_female_id).click()

    def setDataOfBirth(self, birthday):
        self.driver.find_element(By.ID, self.field_date_of_birth_id).clear()
        self.driver.find_element(By.ID, self.field_date_of_birth_id).send_keys(birthday)

    def setCompanyName(self, company):
        self.driver.find_element(By.ID, self.field_company_name_id).clear()
        self.driver.find_element(By.ID, self.field_company_name_id).send_keys(company)

    def setTest(self, test):
        self.driver.find_element(By.ID, self.field_test_id).clear()
        self.driver.find_element(By.ID, self.field_test_id).send_keys(test)

    def setTaxExempt(self):
        self.driver.find_element(By.ID, self.cbox_is_tax_exempt_id).click()

    def setNewsLetter(self, newsletter):
        self.driver.find_element(By.XPATH, self.input_news_letter_xpath).click()
        time.sleep(2)
        if newsletter == "Your store name":
            self.driver.find_element(By.XPATH, self.list_news_letter_option_1_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.list_news_letter_option_2_xpath).click()

    def setCustomerRoles(self, customer):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.input_customer_roles_xpath).click()
        time.sleep(1)
        if customer == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.list_customer_roles_option_1_xpath)
            self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManageVendor(self, vendor):
       select = Select(self.driver.find_element(By.ID, self.dropdown_vendor_id))
       select.select_by_visible_text(vendor)

    def setActive(self):
        time.sleep(2)
        cbox = self.driver.find_element(By.ID, self.cbox_active_id)
        if cbox.get_attribute("checked") != "true":
            cbox.click()

    def setComment(self, comment):
        self.driver.find_element(By.ID, self.field_comment_id).clear()
        self.driver.find_element(By.ID, self.field_comment_id).send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def verifySuccessMessage(self):
        time.sleep(3)
        message = self.driver.find_element(By.XPATH, self.label_success_message_xpath)
        if "The new customer has been added successfully" in message.text:
            assert True
        else:
            assert False


