import time
from selenium.webdriver.support.select import Select
from Locators.Selenium_Path import Locator_Path

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.data = Locator_Path()
        self.driver.find_element_by_name(self.data.Username).send_keys(username)
        time.sleep(2)

    def setPassword(self,password):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.textbox_password_id).send_keys(password)
        time.sleep(2)

    def clickLogin(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.button_login_id).click()
        time.sleep(3)

    def Advance(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Advance).click()
        time.sleep(3)

    def Proceed_link(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Proceed_link).click()
        time.sleep(3)

    def field_gotofolder(self):
        self.data = Locator_Path()
        B = Select(self.driver.find_element_by_id(self.data.field_gotofolder))
        time.sleep(4)
        B.select_by_index(3)
        time.sleep(3)

    def Upload_Wizard(self):
        self.data = Locator_Path()
        self.driver.find_element_by_xpath(self.data.Upload_Wizard).click()
        time.sleep(3)

    def field_gotofolder1(self):
        self.data = Locator_Path()
        B = Select(self.driver.find_element_by_id(self.data.field_gotofolder))
        time.sleep(4)
        B.select_by_index(6)
        time.sleep(3)

    def Last_Page(self):
        self.data = Locator_Path
        self.driver.find_element_by_id(self.data.Last_Page).click()
        time.sleep(3)

    def NewFile(self):
        self.data = Locator_Path()
        self.driver.find_element_by_xpath("//*[@id='cbmenucontainer']/div[1]/img").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='cbmenucontainer']/div[2]/ul/li[4]").click()
        time.sleep(3)
        # i = Select(self.driver.find_element_by_xpath(self.data.NewFile))
        # time.sleep(4)
        # i.select_by_index(3)
        # time.sleep(5)



