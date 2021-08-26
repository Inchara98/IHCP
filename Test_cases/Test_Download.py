import os
import time
from selenium import webdriver
from Page_of_objects.Login_Page import LoginPage
from Utilities.readProperties import ReadConfig
from selenium.webdriver.chrome.options import Options


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    date = ReadConfig.get_date()


    def test_login(self):
        chromeOptions=Options()
        chromeOptions.add_experimental_option("prefs",{"download.default_directory":"/home/inchara/Downloads"})
        self.driver = webdriver.Chrome(executable_path="/home/inchara/PycharmProjects/IHCP/Driver/chromedriver",chrome_options=chromeOptions)
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
        time.sleep(5)
        self.lp.Last_Page()
        time.sleep(2)
        self.lp.NewFile()
        # new_files = "//img[@alt='New File']"
        new_files="//img[@alt='File']"
        files =  self.driver.find_elements_by_xpath(new_files)
        # for i in range(len(files)):
        #     #print(files[i].text, 'links clicked')
        #     files[i].click()
        #     time.sleep(3)
        #
        #     # self.driver.find_element_by_class_name("button btnPrimary").click()
        #     self.driver.back()
        #     time.sleep(5)
        row = 3
        column = 1
        total = self.driver.find_elements_by_xpath("//*[@id='folderfilelisttable']/tbody/tr")

        for i in range(len(total)):
            i=i+1
            checkbox = "//input[@type='checkbox']"+"["+str(i)+"]"
            print(checkbox)
            a=self.driver.find_element_by_xpath(checkbox)
            #a=self.driver.find_element_by_xpath("//*[@id='folderfilelisttable']/tbody/tr["+str(row)+"]/td["+str(column)+"]")
            time.sleep(2)
            print(checkbox,"status=",a.is_selected())
            if a.is_selected() == True:
                print("download icon")
                self.driver.find_element_by_id("downloadLink").click()
                time.sleep(10)
                row = row + 1
                column = column + 1
                print(a,row,column)
                i=0














