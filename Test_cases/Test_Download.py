import time
from selenium import webdriver

from Locators.Selenium_Path import Locator_Path
from Page_of_objects.Login_Page import LoginPage
from Utilities.readProperties import ReadConfig
from selenium.webdriver.chrome.options import Options


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    date = ReadConfig.get_date()


    def test_login(self):

        paths = Locator_Path()
        chromeOptions = Options()
        chromeOptions.add_experimental_option("prefs",{"download.default_directory":""})
        self.driver = webdriver.Chrome(executable_path="",chrome_options=chromeOptions)
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.Advance()
        self.lp.Proceed_link()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)

        newfiles = self.driver.find_elements_by_xpath(paths.Download_files)

        i=12
        while(i<=len(newfiles)):
            download_btn = "//*[@id='content']/tbody/tr["+str(i)+"]/td[2]/span/a[2]"
            self.driver.find_element_by_xpath(download_btn).click()
            time.sleep(6)
            i = i+1
            print(download_btn)






#//*[@id="content"]/tbody/tr[13]/td[2]/span/a[2]









