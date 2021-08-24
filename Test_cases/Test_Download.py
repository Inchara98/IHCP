import time
from selenium import webdriver
from Page_of_objects.Login_Page import LoginPage
from Utilities.readProperties import ReadConfig

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    date = ReadConfig.get_date()

    def test_login(self):
        self.driver = webdriver.Chrome(executable_path="/home/inchara/PycharmProjects/IHCP/Driver/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.Advance()
        self.lp.Proceed_link()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.lp.field_gotofolder1()
        time.sleep(10)
        self.lp.Last_Page()
        time.sleep(3)