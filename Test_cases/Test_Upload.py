import time
from selenium import webdriver
from Page_of_objects.Login_Page import LoginPage
from Utilities.readProperties import ReadConfig

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    Community = ReadConfig.get_Community_FilePath()
    Deaconess = ReadConfig.get_Deaconess_FilePath()
    Downloads = ReadConfig.get_Downloads()
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
        self.lp.field_gotofolder()
        time.sleep(10)
        self.lp.Upload_Wizard()
        time.sleep(4)
        add_files = self.driver.find_element_by_xpath(
            "//*[@id='jswiz-container']/div[2]/div/div/div[2]/div[1]/div[10]/span/input")
        #add_files.send_keys(self.Community)
        time.sleep(2)
        #add_files.send_keys("/home/inchara/Downloads/IHCP Ehealth/GHI/OUTGOING/Deaconess/ELIG_edi_210_GHI_DEAWF2DLY031021")
        time.sleep(2)
        add_files.send_keys(self.Downloads+self.date)
        time.sleep(2)
        #self.driver.find_element_by_xpath("//*[@id='jswiz-container']/div[2]/div/div/div[2]/div[2]/span[2]").click()
        #time.sleep(100)
        self.driver.close()


